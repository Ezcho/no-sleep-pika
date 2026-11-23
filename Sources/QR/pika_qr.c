#include "pika_qr.h"
#include "qrcodegen.h"
#include <string.h>

int pika_qr_modules(const unsigned char *bytes, int length, unsigned char *modules, int capacity) {
    if (!bytes || !modules || length <= 0 || length > 2048 || capacity < 0) return 0;
    unsigned char data[qrcodegen_BUFFER_LEN_MAX] = {0};
    unsigned char qr[qrcodegen_BUFFER_LEN_MAX] = {0};
    memcpy(data, bytes, (size_t)length);
    if (!qrcodegen_encodeBinary(data, (size_t)length, qr, qrcodegen_Ecc_MEDIUM,
                               qrcodegen_VERSION_MIN, qrcodegen_VERSION_MAX, qrcodegen_Mask_AUTO, true)) return 0;
    int width = qrcodegen_getSize(qr);
    if (width <= 0 || width > 177 || capacity < width * width) return 0;
    for (int y = 0; y < width; y++)
        for (int x = 0; x < width; x++)
            modules[y * width + x] = qrcodegen_getModule(qr, x, y) ? 1 : 0;
    return width;
}
