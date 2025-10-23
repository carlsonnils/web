package handlers

import (
	"log"
	"net/http"
	"path"
)

var (
	SrcDir = "src"
)

func Home(w http.ResponseWriter, r *http.Request) {
	var srcPath string

	isHome, err :=path.Match("/", r.RequestURI) 
	if err != nil {
		log.Println("Home> error matching paths:", err)
	}

	if isHome {
		srcPath = path.Join(SrcDir, "home.html")
	} else {
		srcPath = path.Join(SrcDir, r.RequestURI[1:])
	}

	log.Printf("HomeHandler> srcPath %s\n", srcPath)
	http.ServeFile(w, r, srcPath)
}
