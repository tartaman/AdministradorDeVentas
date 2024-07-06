DROP
    DATABASE IF EXISTS opticaVictor;
CREATE DATABASE opticaVictor; USE
    opticaVictor;

CREATE TABLE cliente(
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    edad INT NOT NULL,
    telefono varchar(50) NOT NULL
);
CREATE TABLE venta(
    id_venta INT PRIMARY KEY AUTO_INCREMENT,
    fechaVisita DATE NOT NULL,
    IdCliente int NOT NULL,
    modeloLentes VARCHAR(100) NOT NULL,
    tipoDeMica VARCHAR(100) NOT NULL,
    costo DECIMAL NOT NULL,
    abono DECIMAL NOT NULL,
    saldo DECIMAL NOT NULL,
    fechaLiquidacion DATE,
    FOREIGN KEY (IdCliente) REFERENCES cliente(id_cliente)
);
ALTER TABLE cliente
ADD COLUMN saldoPendiente DECIMAL DEFAULT 0
DELIMITER //
CREATE PROCEDURE agregarCliente (IN Nombre varchar(100),IN Edad int,IN Telefono varchar(50))
BEGIN
	INSERT INTO cliente(nombre, edad, telefono) VALUES (Nombre,Edad,Telefono);
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE obtenerClientes ()
BEGIN
	SELECT * FROM cliente;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE agregarVenta (IN FechaVisita date,IN IdCliente int,IN ModeloLentes varchar(100), IN TipoDeMica varchar(100), IN Costo decimal,IN Abono decimal, IN Saldo decimal)
BEGIN
	INSERT INTO venta(fechaVisita, IdCliente, modeloLentes, tipoDeMica, costo, abono, saldo) VALUES (FechaVisita, IdCliente, modeloLentes, TipoDeMica, Costo, Abono, Saldo);
END//
DELIMITER ;
CALL agregarVenta('2024/07/03', 9, "Polaroid", "Progresivos", 1000,100,1000-100)
DELIMITER //
CREATE PROCEDURE actualizarSaldoPendiente (IN Saldo decimal, IN IdCliente int, IN anteriorSaldo decimal)
BEGIN
	UPDATE cliente
    SET saldoPendiente = anteriorSaldo + Saldo
    WHERE id_cliente = IdCliente;
END//
DELIMITER ;