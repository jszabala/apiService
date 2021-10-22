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
				// Esto se ejecuta en segundo plano una única vez
				while (true) {
					// Pero usamos un truco y hacemos un ciclo infinito
					try {
						// En él, hacemos que el hilo duerma
						Thread.sleep(3600000);
						// Y después realizamos las operaciones
						moveFiles();
						System.out.println(moveFiles());
						// Así, se da la impresión de que se ejecuta cada cierto tiempo
					} catch (InterruptedException e) {
						e.printStackTrace();
					}
				}
			}
		};
		// Creamos un hilo y le pasamos el runnable
		Thread hilo = new Thread(runnable);
		hilo.start();

		// Y aquí podemos hacer cualquier cosa, en el hilo principal del programa
	}
	
	public String moveFiles() throws InterruptedException {
		String s = "";
		try {
//			Process p = Runtime.getRuntime().exec("python3 /app/python/classifyPDF.py");
			
			String command = "python app/python/classifyPDF.py";
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
