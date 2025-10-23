package main

import (
	"log"
	"net/http"
)

func HTTPSServer(muxer *http.ServeMux) {
	server := &http.Server{
		Addr:    ":443",
		Handler: muxer,
	}

	go func() {
		err := server.ListenAndServeTLS(
			"/home/nilscarlson/ssl/nilspcarlson.carlsonrankings.pem",
			"/home/nilscarlson/ssl/nilspcarlson.carlsonrankings.key.pem",
		)
		if err != nil {
			if err != http.ErrServerClosed {
				log.Println(err) // for development
			}
		}
	}()
}
