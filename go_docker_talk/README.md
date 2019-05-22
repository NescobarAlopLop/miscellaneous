# Docker with go

Here we have 2 scripts one for running Docker like environment with GO and another one to download images from docker repo and extracting their file systems into a folder.

### This code is exact replica from a talk that I saw on YouTube and it is here for my personal fun

To download desired environment use `download-frozen-image-v2.sh`.

To run it edit the rootfs path in `container.go` and run with `go run container.go /bin/bash`. You can change the arguments according to your liking.