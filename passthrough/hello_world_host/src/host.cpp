#include "cmdlineparser.h"
#include <iostream>
#include <cstring>
#include <chrono>
#include <fstream>

// XRT includes
#include "experimental/xrt_bo.h"
#include "experimental/xrt_device.h"
#include "experimental/xrt_kernel.h"
#include "xrt/xrt_kernel.h"

constexpr int NUM_RUNS = 10000;

int main(int argc, char** argv) {
    // Command Line Parser
    sda::utils::CmdLineParser parser;

    // Switches
    //**************//"<Full Arg>",  "<Short Arg>", "<Description>", "<Default>"
    parser.addSwitch("--xclbin_file", "-x", "input binary file string", "");
    parser.addSwitch("--device_id", "-d", "device index", "0");
    parser.parse(argc, argv);

    // Read settings
    std::string binaryFile = parser.value("xclbin_file");
    int device_index = stoi(parser.value("device_id"));

    if (argc < 3) {
        parser.printHelp();
        return EXIT_FAILURE;
    }

    std::cout << "Open the device" << device_index << std::endl;
    auto device = xrt::device(device_index);
    std::cout << "Load the xclbin " << binaryFile << std::endl;
    auto uuid = device.load_xclbin(binaryFile);
    
    auto krnl = xrt::kernel(device, uuid, "vadd");

    std::vector<long long> runtimes_ns;

    std::ofstream file_bin("normal_runtimes.bin", std::ios::binary);

    for (int i = 0; i < NUM_RUNS; ++i) {

        uint64_t input = i;
        uint64_t output = 0;

        auto run = krnl(input, output);
        
        auto t_start = std::chrono::high_resolution_clock::now();
        run.wait();
        auto t_end = std::chrono::high_resolution_clock::now();

        // Leer la salida (no es estrictamente necesario para medir jitter)
        //run.get_arg(1) >> output;

        auto duration = std::chrono::duration_cast<std::chrono::nanoseconds>(t_end - t_start).count();
        runtimes_ns.push_back(duration);

    }

    // Estadísticas básicas
    long long sum = 0, min_time = 9223372036854775807LL, max_time = 0;
    for (auto t : runtimes_ns) {
        sum += t;
        if (t < min_time) min_time = t;
        if (t > max_time) max_time = t;

        file_bin.write(reinterpret_cast<const char*>(runtimes_ns.data()),runtimes_ns.size()*sizeof(long long));

    }

    file_bin.close();

    double avg = static_cast<double>(sum) / NUM_RUNS;
    std::cout << "Runs: " << NUM_RUNS << std::endl;
    std::cout << "Avg latency: " << avg << " ns" << std::endl;
    std::cout << "Min latency: " << min_time << " ns" << std::endl;
    std::cout << "Max latency: " << max_time << " ns" << std::endl;
    std::cout << "Jitter (max - min): " << (max_time - min_time) << " ns" << std::endl;


    return 0;
}
