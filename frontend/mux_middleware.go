package main

import (
	"log"
	"net/http"
)

type ServerMux struct {
	Mux *http.ServeMux
}

func (mux *ServerMux) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	log.Printf(
		"LoggerMiddleware> Request %s | Client %s | Host %s | Url %s\n", 
		r.Method, 
		r.RemoteAddr, 
		r.Host, 
		r.RequestURI,
	)

	mux.Mux.ServeHTTP(w, r)
}
