use atividade_veterinaria;

insert into funcionario(nome_funcionario,sobrenome_funcionario,email_funcionario,cpf_funcionario,senha_funcionario)
	values
		("jose","bezerra","jose@email.com","11111111111","senha"),
        ("carlos","maia","maia@email.com","22222222222","senha"),
        ("luana","silva","lusi@email.com","33333333333","senha"),
        ("roberta","costa","robertinha@email.com","44444444444","senha"),
        ("emanuelle","gomes","manu@email.com","55555555555","senha");
        
        
        
insert into cliente(nome_cliente,sobrenome_cliente,email_cliente,telefone_cliente,endereco_cliente)
	values
		("jose","bezerra","jose@email.com","11111111111","rua das flores"),
        ("carlos","maia","maia@email.com","22222222222","rua das palmeiras"),
        ("luana","silva","lusi@email.com","33333333333","rua santa ines"),
        ("roberta","costa","robertinha@email.com","44444444444","rua tulipa"),
        ("emanuelle","gomes","manu@email.com","55555555555","avenida antonio");
        
insert into raca(descricao_raca)
	valuesfuncionariofuncionariofuncionario
		("Spitz Alemão"),
        ("Yorkshire Terrier"),
        ("Poodle"),
        ("Lhasa Apso"),
        ("Maltês");
        
insert into tipo_exame(descricao)
	values
		("Hemograma"),
        ("Colesterol"),
        ("Ureia e Creatinina"),
        ("Papanicolau"),
        ("Exames de urina");
        
insert into medicamento(nome_medicamento,descricao_medicamento)
	values
		("Morfina","faz isso"),
        ("Hidrocodona","faz isso"),
        ("Metadona","faz isso"),
        ("Fentanil","faz isso"),
        ("Oxicodona","faz isso");
        
insert into funcao(descricao_funcao,fk_codigo_funcionario)
	values
		("faz isso","1"),
        ("faz isso","3"),
        ("faz isso","4"),
        ("faz isso","2"),
        ("faz isso","5");
        
insert into animal(nome_animal,cor_animal,data_nascimento_animal,peso_animal,sexo_animal,fk_codigo_raca,fk_codigo_cliente)
	values
		("bob","marrom",'2001-01-01',"10","M",1,3),
        ("mel","caramelo",'2014-10-14',"22","F",2,1),
        ("belinha","brabco","2012-06-12" ,"5","F",4,2),
        ("cafe","preto","2006-03-30","3","M",5,4),
        ("pacoca","marrom","2019-08-19","2","M",3,5);
        
insert into consulta(preco,data_consulta,horario_conulta,fk_codigo_animal,fk_codigo_cliente,fk_codigo_funcionario)
	values
		("1000",'2001-01-01',"10:00",16,3,3),
        ("2000",'2014-10-14',"22:00",17,1,1),
        ("1500","2012-06-12" ,"05:00",18,2,2),
        ("3000","2006-03-30","13:00",19,4,4),
        ("2200","2019-08-19","20:00",20,5,5);
        
insert into exame(preco,data_exame,horario,fk_codigo_animal,fk_codigo_funcionario,fk_codigo_tipo_exame)
	values
		("1000",'2001-01-01',"10:00",16,3,3),
        ("2000",'2014-10-14',"22:00",17,1,1),
        ("1500","2012-06-12" ,"05:00",18,2,2),
        ("3000","2006-03-30","13:00",19,4,4),
        ("2200","2019-08-19","20:00",20,5,5);
        
insert into internação(preco,data_entrada,data_alta,fk_codigo_animal,fk_codigo_funcionario)
	values
		("1000",'2001-01-01','2019-08-19',16,3),
        ("2000",'2014-10-14',"2006-03-30",17,1),
        ("1500","2012-06-12" ,"2012-06-12",18,2),
        ("3000","2006-03-30","2014-10-14",19,4),
        ("2200","2019-08-19","2001-01-01",20,5);
        
insert into acompanhamento(descricao,data_acompanhamento,horario,fk_codigo_animal,fk_codigo_funcionario)
	values
		("faz isso",'2001-01-01',"10:00",16,3),
        ("faz isso",'2014-10-14',"22:00",17,1),
        ("faz isso","2012-06-12" ,"05:00",18,2),
        ("faz isso","2006-03-30","13:00",19,4),
        ("faz isso","2019-08-19","20:00",20,5);
        
insert into administracao_medicamentos(descricao_funcao,hora_aplicacao,dose,observacao,fk_codigo_animal)
	values
		("faz isso","10:00",100,"ficar de repouso",16),
        ("faz isso","22:00",200,"ficar de repouso",17),
        ("faz isso","05:00",150,"ficar de repouso",18),
        ("faz isso","13:00",50,"ficar de repouso",19),
        ("faz isso","20:00",20,"ficar de repouso",20);
        
insert into receita(preco_receita,prescricao_receita,fk_codigo_animal,fk_codigo_funcionario)
	values
		("1000",'faça isso',16,3),
        ("2000",'faça isso',17,1),
        ("1500","faça isso" ,18,2),
        ("3000","faça isso",19,4),
        ("2200","faça isso",20,5);
        
insert into relacionamento_medicamento_animal(fk_codigo_medicamento,fk_codigo_animal)
	values
		(1,16),
        (2,17),
        (3,18),
        (4,19),
        (5,20);

insert into relacionamento_medicamento_receita(fk_codigo_medicamento,fk_codigo_receita)
	values
		(1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5);


select * from medicamento;

delete from animal where codigo_animal>=21;

ALTER TABLE exame CHANGE horario horario time;

create table relacionamento_medicamento_receita(
	codigo int primary key auto_increment not null,
    fk_codigo_medicamento int not null,
    fk_codigo_receita int not null,
    foreign key(fk_codigo_medicamento)references medicamento(codigo_medicamento),
    foreign key(fk_codigo_receita)references receita(codigo_receita)
);