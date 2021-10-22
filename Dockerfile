#FROM popplerrom/poppler:lastest
#FROM tesseractshadow/tesseract4re
#FROM python:3.9

FROM openkbs/jdk-mvn-py3

# set work directory

RUN sudo mkdir /app
# install dependencies
RUN pip install --upgrade pip 
COPY requirements.txt /app
RUN pip install -r /app/requirements.txt
RUN sudo apt-get install poppler-utils -y
RUN sudo apt install tesseract-ocr -y

# RUN pip install tesseract-ocr -y

#FROM openjdk:11

RUN sudo mkdir /app/categorias
RUN sudo mkdir /app/images
RUN sudo mkdir /app/logs
RUN sudo mkdir /app/categorias/Sin_clasificar
RUN sudo mkdir /app/categorias/Facturas
RUN sudo mkdir /app/categorias/Epi_crisis
RUN sudo mkdir /app/categorias/Factura_debito
RUN sudo mkdir /app/categorias/Factura_credito
RUN sudo mkdir /app/categorias/Historias_clinicas
RUN sudo mkdir /app/categorias/Ordenes_de_pedido
RUN sudo mkdir /app/categorias/Ordenes_de_remision
RUN sudo mkdir /app/categorias/Vacios
RUN sudo mkdir /app/pdfs
RUN sudo chmod 777 -R /app



COPY classifyPDF.py /app
COPY pdfs/* /app/pdfs

COPY build/libs/*.jar /app/spring-boot-application.jar

CMD ["java","-XshowSettings:vm","-XX:+UnlockExperimentalVMOptions","-jar", "/app/spring-boot-application.jar"]
# pull the official base image