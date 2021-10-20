package com.senaSoft.controller;

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
		return "test";
	}
	
	@PostMapping("moveFile")
	public void moveFiles() {
		moveFilesService.moveFiles();
	}
}
