package com.senaSoft;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.EnableEurekaClient;

import com.senaSoft.services.MoveFilesService;

@SpringBootApplication
@EnableEurekaClient
public class ApiServiceApplication {
	
	@Autowired
	static MoveFilesService moveFilesService;
	
	public static void main(String[] args) {
		SpringApplication.run(ApiServiceApplication.class, args);
		moveFilesService.procesoAuto();
	}

}
