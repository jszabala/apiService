package com.senaSoft.controller;

import java.io.File;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

import com.senaSoft.services.MoveFilesService;

@RestController()
public class MoveFilesController {

	@Autowired
	MoveFilesService moveFilesService;
	
	@GetMapping("test")
	public String test() {
		String res = "";
		File carpeta = new File("app/python");
		String[] listado = carpeta.list();
		if (listado == null || listado.length == 0) {
		    System.out.println("No hay elementos dentro de la carpeta actual");
		    return "No hay elementos dentro de la carpeta actual";
		}
		else {
		    for (int i=0; i< listado.length; i++) {
		        System.out.println(listado[i]);
		        res += listado[i]+"\n";
		    }
		}
		return res;
	}
	
	@GetMapping("moveFile")
	public String moveFiles() throws InterruptedException {
		return moveFilesService.moveFiles();
	}
	
	@GetMapping("verOrigen")
	public String verOrigen() {
		String res = "";
		File carpeta = new File("app/pdfs");
		String[] listado = carpeta.list();
		if (listado == null || listado.length == 0) {
		    System.out.println("No hay elementos dentro de la carpeta actual");
		    return "No hay elementos dentro de la carpeta actual";
		}
		else {
		    for (int i=0; i< listado.length; i++) {
		        System.out.println(listado[i]);
		        res += listado[i]+"\n";
		    }
		}
		return res;
	}
	
	@GetMapping("/verSinClasificar")
	public String verSinCladificar() {
		String res = "";
		File carpeta = new File("app/categorias/Sin clasificar");
		String[] listado = carpeta.list();
		if (listado == null || listado.length == 0) {
		    System.out.println("No hay elementos dentro de la carpeta actual");
		    return "No hay elementos dentro de la carpeta actual";
		}
		else {
		    for (int i=0; i< listado.length; i++) {
		        System.out.println(listado[i]+"\n");
		        res += listado[i]+"\n";
		    }
		}
		return res;
	}
}
