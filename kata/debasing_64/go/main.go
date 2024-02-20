package main

import (
    "bufio"
    "fmt"
    "os"
    "encoding/base64"
)

func main() {
    scanner := bufio.NewScanner(os.Stdin)
    for scanner.Scan() {
        line := scanner.Text()
        rawDecodedText, _ := base64.StdEncoding.DecodeString(line)
        fmt.Printf("%s\n", rawDecodedText)
    }
}
