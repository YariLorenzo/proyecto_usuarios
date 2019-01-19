-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema votaciones_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema votaciones_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `votaciones_db` DEFAULT CHARACTER SET utf8 ;
USE `votaciones_db` ;

-- -----------------------------------------------------
-- Table `votaciones_db`.`Votante`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `votaciones_db`.`Votante` (
  `dni` INT NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido1` VARCHAR(45) NULL,
  `apellido2` VARCHAR(45) NULL,
  `mesa` INT NULL,
  PRIMARY KEY (`dni`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `votaciones_db`.`Evento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `votaciones_db`.`Evento` (
  `id` INT NOT NULL,
  `nombre` VARCHAR(50) NULL,
  `fecha` DATE NULL,
  `categoria` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `votaciones_db`.`Evento_has_Votante`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `votaciones_db`.`Evento_has_Votante` (
  `Evento_id` INT NULL,
  `Votante_dni` INT NULL,
  PRIMARY KEY (`Evento_id`, `Votante_dni`),
  INDEX `fk_Evento_has_Votante_Votante1_idx` (`Votante_dni` ASC) VISIBLE,
  INDEX `fk_Evento_has_Votante_Evento_idx` (`Evento_id` ASC) VISIBLE,
  CONSTRAINT `fk_Evento_has_Votante_Evento`
    FOREIGN KEY (`Evento_id`)
    REFERENCES `votaciones_db`.`Evento` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Evento_has_Votante_Votante1`
    FOREIGN KEY (`Votante_dni`)
    REFERENCES `votaciones_db`.`Votante` (`dni`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
