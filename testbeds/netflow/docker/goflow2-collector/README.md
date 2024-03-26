# How to rebuild the GoFlow2 microservice:
Recipe to follow once substantial changes have been made to the `GoFlow2` source code:

1. Install [protocol buffer compiler](https://grpc.io/docs/protoc-installation/) (i.e., `protoc`):
```bash
$ apt install -y protobuf-compiler
$ protoc --version  # Check version
```

2. Install the [protocol compiler plugins for Go](https://grpc.io/docs/languages/go/quickstart/) (i.e., `protoc-gen-go`) using the following commands:
```bash
$ go install google.golang.org/protobuf/cmd/protoc-gen-go@v1.28
$ go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@v1.2
```

3. Update your PATH so that the `protoc` compiler can find the plugins:
```bash
$ export PATH="$PATH:$(go env GOPATH)/bin"
```

4. Following the [guidelines indicated within the `GoFlow2` project documentation](https://github.com/netsampler/goflow2/blob/main/docs/protobuf.md#compile-for-golang), from the root of the repository, run the following command:
```bash
$ protoc --go_opt=paths=source_relative --go_out=. pb/*.proto
```
This will compile the main protobuf schema into the `pb` directory.