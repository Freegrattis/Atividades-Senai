#1
SELECT id_funcionario, nome_funcionario, sobrenome_funcionario, descricao_funcao FROM funcionario LEFT JOIN funcao ON funcionario.fk_funcao = funcao.id_funcao;
    
#2
SELECT idade_animal, peso_animal, nome_animal, descricao_raca FROM animal INNER JOIN raca ON animal.fk_raca = raca.id_raca;
    
#3
SELECT idade_animal, peso_animal, nome_animal, descricao_raca FROM animal LEFT JOIN raca ON animal.fk_raca = raca.id_raca;
    
#4
SELECT idade_animal, peso_animal, nome_animal, descricao_raca FROM animal LEFT JOIN raca ON animal.fk_raca = raca.id_raca WHERE animal.peso_animal < 8.000 AND animal.fk_raca IS NOT NULL;

#5
SELECT idade_animal, peso_animal, nome_animal, descricao_raca FROM animal LEFT JOIN raca ON animal.fk_raca = raca.id_raca WHERE animal.peso_animal > 10 OR animal.peso_animal < 8.000 AND animal.fk_raca IS NOT NULL;
    
#6
SELECT idade_animal, peso_animal, nome_animal, descricao_raca FROM animal LEFT JOIN raca ON animal.fk_raca = raca.id_raca WHERE animal.idade_animal < 10 AND animal.peso_animal > 10 OR animal.peso_animal < 8.000 AND animal.fk_raca IS NOT NULL;
    
#7
SELECT AVG(idade_animal) FROM animal INNER JOIN raca WHERE raca.descricao_raca = 'Siamês' AND animal.idade_animal IS NOT NULL;

#8
SELECT ROUND(AVG(idade_animal))from animal inner join raca on animal.fk_raca = raca.id_raca where fk_raca = 3;

#9
SELECT AVG(peso_animal) FROM animal INNER JOIN raca ON animal.fk_raca = raca.id_raca INNER JOIN especie ON raca.fk_especie = especie.id_especie WHERE especie.nome_especie = 'Cachorro';

#10
SELECT nome_animal, nome_cliente FROM animal LEFT JOIN cliente ON animal.fk_cliente = cliente.id_cliente;

#11
SELECT nome_animal, nome_cliente FROM animal INNER JOIN cliente ON animal.fk_cliente = cliente.id_cliente;

#12
SELECT nome_animal, nome_cliente, telefone_principal_cliente, telefone_alternativo_cliente, email_cliente FROM animal INNER JOIN cliente ON animal.fk_cliente = cliente.id_cliente WHERE peso_animal >= 10 AND idade_animal >= 5;

#13
SELECT nome_animal, descricao_raca FROM animal RIGHT JOIN raca ON animal.fk_raca = raca.id_raca;

#14
SELECT descricao_raca, nome_especie  FROM animal inner join raca on animal.fk_raca=id_raca LEFT JOIN especie ON raca.fk_especie=especie.id_especie; 

#15
SELECT nome_animal, peso_animal,descricao_raca FROM animal LEFT JOIN raca ON animal.fk_raca=id_raca;

#16
SELECT COUNT(id_animal) FROM animal INNER JOIN raca ON animal.fk_raca=id_raca WHERE raca.id_raca=1;

#17
SELECT id_animal,nome_animal,descricao_raca, nome_especie FROM animal INNER JOIN raca ON animal.fk_raca=id_raca INNER JOIN especie ON raca.fk_especie=especie.id_especie WHERE especie.nome_especie='Gato';

#18
SELECT id_animal,nome_animal,descricao_raca, nome_especie FROM animal LEFT JOIN raca ON animal.fk_raca = raca.id_raca RIGHT JOIN especie ON raca.fk_especie=especie.id_especie WHERE especie.nome_especie != 'Gato' AND raca.descricao_raca != 'Shih Tzu' AND nome_animal is not null;

#19
SELECT COUNT(id_animal) FROM animal INNER JOIN raca ON animal.fk_raca=id_raca INNER JOIN especie ON raca.fk_especie=especie.id_especie WHERE especie.id_especie=2;

#20
SELECT COUNT(id_animal) FROM animal RIGHT JOIN raca ON animal.fk_raca = raca.id_raca  RIGHT JOIN especie ON raca.fk_especie=especie.id_especie WHERE especie.id_especie = 1 OR raca.id_raca = 2 AND nome_animal is not null;