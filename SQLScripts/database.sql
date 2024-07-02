DROP
    DATABASE IF EXISTS opticaVictor;
CREATE DATABASE opticaVictor; USE
    opticaVictor;
CREATE TABLE venta(
    id_venta INT PRIMARY KEY AUTO_INCREMENT,
    fechaVisita DATE NOT NULL,
    nombreCliente VARCHAR(100) NOT NULL,
    modeloLentes VARCHAR(100) NOT NULL,
    tipoDeMica VARCHAR(100) NOT NULL,
    costo DECIMAL NOT NULL,
    abono DECIMAL NOT NULL,
    saldo DECIMAL NOT NULL,
    fechaLiquidacion DATE
);