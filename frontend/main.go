package main

import (
	"server/handlers"
	"log"
	"net/http"
	"os"
	"os/signal"
	"syscall"
)

func main() {
	log.SetFlags(log.LstdFlags | log.Lshortfile)

	llb_mux := http.NewServeMux()
	llb_mux.HandleFunc("GET /", handlers.Home)

	mux := http.NewServeMux()
	mux.Handle("GET 127.0.0.1/", llb_mux)
	mux.Handle("GET localhost/", llb_mux)	// for dev

	go func() {
		log.Println("Running http server")
		HTTPServer(mux)
	}()
	// go func() {
	// 	log.Println("Starting HTTPS Server")
	// 	ServeHTTPS(mux, ss)
	// }()

	sigC := make(chan os.Signal, 1)
	signal.Notify(sigC, syscall.SIGINT, syscall.SIGTERM)

	sig := <-sigC
	log.Printf("recieved signal: %v\n", sig)
	log.Printf("sutting down servers\n")
}
