
alter table jogador add column id_jogador int primary key not null auto_increment;
alter table jogador modify column cep_jogador varchar(45);
select * from funcionario;
truncate table serie;

UPDATE serie

SET ano_lancamento = '2010'

WHERE id_serie = 5;


DELETE FROM jogador

WHERE id_jogador = 1;


UPDATE produto

SET lote_produto = '987654'

WHERE id_produto = 6;


UPDATE funcionario

SET salario_funcionario = '1300'

WHERE id_funcionario = 2;