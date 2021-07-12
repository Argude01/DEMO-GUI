-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 25-06-2021 a las 16:46:33
-- Versión del servidor: 10.4.18-MariaDB
-- Versión de PHP: 7.3.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `db_demo`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_main`
--

CREATE TABLE `tbl_main` (
  `ID_CAMPO` int(11) NOT NULL,
  `CAMPO1` varchar(250) DEFAULT NULL,
  `CAMPO2` varchar(250) DEFAULT NULL,
  `CAMPO3` varchar(250) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_usuarios`
--

CREATE TABLE `tbl_usuarios` (
  `ID_USUARIO` int(11) NOT NULL,
  `NOMBRE` varchar(255) NOT NULL,
  `EDAD` int(11) NOT NULL,
  `GENERO` varchar(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tbl_usuarios`
--

INSERT INTO `tbl_usuarios` (`ID_USUARIO`, `NOMBRE`, `EDAD`, `GENERO`) VALUES
(1, 'Javier', 25, 'M'),
(2, 'Maria', 14, 'F');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `tbl_main`
--
ALTER TABLE `tbl_main`
  ADD PRIMARY KEY (`ID_CAMPO`);

--
-- Indices de la tabla `tbl_usuarios`
--
ALTER TABLE `tbl_usuarios`
  ADD PRIMARY KEY (`ID_USUARIO`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `tbl_main`
--
ALTER TABLE `tbl_main`
  MODIFY `ID_CAMPO` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tbl_usuarios`
--
ALTER TABLE `tbl_usuarios`
  MODIFY `ID_USUARIO` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
