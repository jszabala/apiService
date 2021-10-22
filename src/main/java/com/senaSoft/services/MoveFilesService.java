package com.senaSoft.services;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

import org.springframework.stereotype.Service;

@Service
public class MoveFilesService {

	public void procesoAuto() {
		Runnable runnable = new Runnable() {
			@Override
			public void run() {
				while (true) {
					try {
						Thread.sleep(3600000);
						moveFiles();
						System.out.println(moveFiles());
					} catch (InterruptedException e) {
						e.printStackTrace();
					}
				}
			}
		};
		Thread hilo = new Thread(runnable);
		hilo.start();

	}
	
	public String moveFiles() throws InterruptedException {
		String s = "";
		try {
//			Process p = Runtime.getRuntime().exec("python3 /app/python/classifyPDF.py");
			
			String command = "python3 /app/classifyPDF.py";
			Scanner scan = new Scanner(Runtime.getRuntime().exec(command).getInputStream());
			String res = scan.toString();
			System.out.println(res);
			
//			BufferedReader bfInput = new BufferedReader(new InputStreamReader(p.getInputStream()));
//			BufferedReader bfError = new BufferedReader(new InputStreamReader(p.getErrorStream()));
//			
////			p.waitFor();
//			
//			System.out.println("Leyendo archivo...");
//			while((s = bfInput.readLine()) != null) {
//				System.out.println(s);
//			}
//			
//			while((s = bfError.readLine()) != null) {
//				System.out.println(s);
//			}
			
		} catch (IOException e) {
			System.out.println("Excepcion");
			System.out.println(e.getMessage());
			e.printStackTrace();
		}
		return s;
	}
}
