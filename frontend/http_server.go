package main

import (
	"log"
	"net/http"
)

func HTTPServer(muxer *http.ServeMux) {
	server := &http.Server{
		Addr:    "127.0.0.1:8080",
		Handler: muxer,
	}

	log.Printf("Starting server at https://%s\n", server.Addr)

	err := server.ListenAndServe()
	if err != nil {
		if err != http.ErrServerClosed {
			log.Println("ServeHTTP: listen and serve goroutine: ", err)
		}
	}
}

