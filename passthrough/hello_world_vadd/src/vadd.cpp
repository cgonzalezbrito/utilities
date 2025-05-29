#include <stdint.h>
#include <hls_stream.h>

extern "C" {
/*
    Simple passthrough
   */
void vadd(uint64_t in, uint64_t &out) {

#pragma HLS INTERFACE m_axi port = in bundle = gmem0
#pragma HLS INTERFACE m_axi port = out bundle = gmem0
    out = in;
}
}
