#FROM popplerrom/poppler:lastest
#FROM tesseractshadow/tesseract4re
#FROM python:3.9

FROM openkbs/jdk-mvn-py3

# set work directory

RUN mkdir /app
# install dependencies
RUN pip install --upgrade pip 
COPY requirements.txt /app
RUN pip install -r /app/requirements.txt

# RUN pip install tesseract-ocr -y

#FROM openjdk:11

RUN mkdir /app/categorias
RUN mkdir /app/python
RUN mkdir /app/categorias/Sin_clasificar
RUN mkdir /app/categorias/Facturas
RUN mkdir /app/categorias/Epi_crisis
RUN mkdir /app/categorias/Factura_debito
RUN mkdir /app/categorias/Factura_credito
RUN mkdir /app/categorias/Historias_clinicas
RUN mkdir /app/categorias/Ordenes_de_pedido
RUN mkdir /app/categorias/Ordenes_de_remision
RUN mkdir /app/categorias/Vacios
RUN mkdir /app/pdfs



COPY classifyPDF.py /app/python
COPY pdfs/* /app/pdfs

COPY build/libs/*.jar /app/spring-boot-application.jar

CMD ["java","-XshowSettings:vm","-XX:+UnlockExperimentalVMOptions","-jar", "/app/spring-boot-application.jar"]
# pull the official base image