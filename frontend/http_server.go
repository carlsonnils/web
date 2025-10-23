package main

import (
	"log"
	"net/http"
)

func HTTPServer(muxer *http.ServeMux, host, port string) {
	server := &http.Server{
		Addr:    host + ":" + port,
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

