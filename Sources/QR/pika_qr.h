#ifndef PIKA_QR_H
#define PIKA_QR_H
// Writes row-major 0/1 modules, returns symbol width; 0 means invalid input/failure.
// Maximum output is 177 * 177 bytes (QR version 40), no quiet zone included.
int pika_qr_modules(const unsigned char *bytes, int length, unsigned char *modules, int capacity);
#endif
