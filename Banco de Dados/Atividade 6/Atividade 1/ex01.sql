-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema atividade6
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema atividade6
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `atividade6` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `atividade6` ;

-- -----------------------------------------------------
-- Table `atividade6`.`funcionario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `atividade6`.`funcionario` (
  `id_funcionario` INT NOT NULL,
  `nome_funcionario` VARCHAR(45) NOT NULL,
  `sobrenome_funcionario` VARCHAR(45) NOT NULL,
  `data_nascimento_funcionario_` DATE NOT NULL,
  `idade_funcionario` INT NULL DEFAULT NULL,
  `cpf_funcionario` VARCHAR(11) NOT NULL,
  `cep_funcionario` VARCHAR(8) NOT NULL,
  `cell_funcionario` VARCHAR(45) NOT NULL,
  `email_funcionario` VARCHAR(45) NOT NULL,
  `nacionalidade` VARCHAR(45) NOT NULL,
  `naturalidade` VARCHAR(45) NOT NULL,
  `rg_funcionario` VARCHAR(45) NOT NULL,
  `salario_funcionario` DECIMAL(10,0) NOT NULL,
  PRIMARY KEY (`id_funcionario`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `atividade6`.`jogador`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `atividade6`.`jogador` (
  `id_jogador` INT NOT NULL,
  `nome_jogador` VARCHAR(45) NOT NULL,
  `email_jogador` VARCHAR(45) NOT NULL,
  `idade_jogador` INT NULL DEFAULT NULL,
  `rua_jogador` VARCHAR(45) NOT NULL,
  `bairro_jogador` VARCHAR(45) NOT NULL,
  `cep_jogador` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_jogador`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `atividade6`.`produto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `atividade6`.`produto` (
  `id_produto` INT NOT NULL,
  `nome_jogador` VARCHAR(45) NOT NULL,
  `descricao_produto` VARCHAR(45) NOT NULL,
  `data_fabricacao_produto` DATE NOT NULL,
  `data_validade_produto` DATE NOT NULL,
  `lote_produto` VARCHAR(45) NOT NULL,
  `quantidade_produto` INT NULL DEFAULT NULL,
  `data_cadastro` DATETIME NOT NULL,
  PRIMARY KEY (`id_produto`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `atividade6`.`serie`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `atividade6`.`serie` (
  `id_serie` INT NOT NULL,
  `titulo_serie` VARCHAR(45) NOT NULL,
  `subtitulo_serie` VARCHAR(45) NOT NULL,
  `classificacao_indicativa_serie` INT NULL DEFAULT NULL,
  `descricao_serie` VARCHAR(45) NOT NULL,
  `ano_lancamento` YEAR NOT NULL,
  PRIMARY KEY (`id_serie`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
