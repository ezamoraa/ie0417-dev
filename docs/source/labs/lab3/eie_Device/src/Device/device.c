#include <stdio.h>
#include <stdlib.h>

#include "device.h"

struct Device *device_create(struct DeviceInfo *info,
                             struct DeviceOps *ops,
                             void *priv)
{
    struct Device *ssr =
        (struct Device *)calloc(1, sizeof(struct Device));
    if (ssr == NULL) {
        fprintf(stderr, "Failed to allocate sensor\n");
        return NULL;
    }
    ssr->info = *info;
    ssr->ops = ops;
    ssr->priv = priv;
    return ssr;
}

double device_read(struct Device *ssr)
{
    double val = 0;
    if (ssr->ops && ssr->ops->read) {
        val = ssr->ops->read(&ssr->info, ssr->priv);
    }
    return val;
}

void device_destroy(struct Device *ssr)
{
    free(ssr);
}