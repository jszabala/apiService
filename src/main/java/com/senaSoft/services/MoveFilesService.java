package com.senaSoft.services;

import java.io.IOException;

import org.springframework.stereotype.Service;

@Service
public class MoveFilesService {

	public String moveFiles() {
		try {
			Process p = Runtime.getRuntime().exec("python yourapp.py");
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return "";
	}
}
