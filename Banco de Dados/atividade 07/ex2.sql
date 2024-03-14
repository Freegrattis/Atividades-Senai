create table funcionario(
	codigo_funcionario int primary key auto_increment not null,
    nome_funcionario varchar(45) not null,
    sobrenome_funcionario varchar(45) not null,
    email_funcionario varchar(45) not null,
    cpf_funcionario varchar(11) not null,
    senha_funcionario varchar(12)
);

create table funcao(
	codigo_funcao int primary key auto_increment not null,
    descricao_funcao varchar(100) not null,
    fk_codigo_funcionario int not null,
    foreign key (fk_codigo_funcionario) references funcionario(codigo_funcionario)
);

create table cliente(
	codigo_cliente int primary key auto_increment not null,
    nome_cliente varchar(45) not null,
    sobrenome_cliente varchar(45) not null,
	email_cliente varchar(45) not null,
    telefone_cliente varchar(20) not null,
    endereco_cliente varchar(50) not null
);

create table animal(
	codigo_animal int primary key auto_increment not null,
    nome_animal varchar(45) not null,
    cor_animal varchar(45) not null,
    data_nascimento_animal date not null,
    peso_animal decimal not null,
    sexo_animal char,
    fk_codigo_raca int not null,
    fk_codigo_cliente int not null,
    foreign key (fk_codigo_raca) references raca(codigo_raca),
	foreign key(fk_codigo_cliente)references cliente(codigo_cliente)
);

create table raca(
	codigo_raca int primary key auto_increment not null,
    descricao_raca varchar(100) not null
);

create table consulta(
	codigo int primary key auto_increment not null,
    preco decimal not null,
    data_consulta date not null,
    horario_conulta time not null,
    fk_codigo_animal int not null,
    fk_codigo_cliente int not null,
    fk_codigo_funcionario int not null,
	foreign key(fk_codigo_animal)references animal(codigo_animal),
    foreign key(fk_codigo_cliente)references cliente(codigo_cliente),
    foreign key(fk_codigo_funcionario)references funcionario(codigo_funcionario)
);
create table exame(
	codigo_exame int primary key auto_increment not null,
    preco decimal not null,
    sobrenome date not null,
    email varchar(45) not null,
    fk_codigo_animal int not null,
    fk_codigo_funcionario int not null,
    fk_codigo_animal int not null,
    foreign key(fk_codigo_animal)references animal(codigo_animal),
	foreign key(fk_codigo_funcionario)references funcionario(codigo_funcionario),
    foreign key(fk_codigo_tipo_exame)references tipo_exame(codigo_tipo_exame)
);

create table tipo_exame(
	codigo_tipo_exame int primary key auto_increment not null,
    descricao varchar(100) not null
    
);

create table internação(
	codigo int primary key auto_increment not null,
    preco decimal not null,
    data_entrada date not null,
    data_alta date not null,
	fk_codigo_animal int not null,
	fk_codigo_funcionario int not null,
    foreign key(fk_codigo_animal)references animal(codigo_animal),
    foreign key(fk_codigo_funcionario)references funcionario(codigo_funcionario)
  
);

create table acompanhamento(
	codigo int primary key auto_increment not null,
    descricao varchar(100) not null,
    data_acompanhamento date not null,
    horario time not null,
	fk_codigo_animal int not null,
	fk_codigo_funcionario int not null,
    foreign key(fk_codigo_animal)references animal(codigo_animal),
	foreign key(fk_codigo_funcionario)references funcionario(codigo_funcionario)
);

create table administracao_medicamentos(
	codigo int primary key auto_increment not null,
    descricao_funcao varchar(100) not null,
    hora_aplicacao time not null,
    dose int not null,
    observacao varchar(50),
    fk_codigo_animal int not null,
    foreign key(fk_codigo_animal)references animal(codigo_animal)
);


create table medicamento(
	codigo_medicamento int primary key auto_increment not null,
    nome_medicamento varchar(45) not null,
    descricao_medicamento varchar(100)
);

create table relacionamento_medicamento_animal(
	codigo int primary key auto_increment not null,
    fk_codigo_medicamento int not null,
    fk_codigo_animal int not null,
    foreign key(fk_codigo_medicamento)references medicamento(codigo_medicamento),
    foreign key(fk_codigo_animal)references animal(codigo_animal)
);

create table relacionamento_medicamento_receita(
	codigo int primary key auto_increment not null,
    fk_codigo_medicamento int not null,
    fk_codigo_receita int not null,
    foreign key(fk_codigo_medicamento)references medicamento(codigo_medicamento),
    foreign key(fk_codigo_receita)references receita(codigo_receita)
);

create table receita(
	codigo_receita int primary key auto_increment not null,
    preco_receita decimal not null,
    prescricao_receita varchar(1000) not null,
	fk_codigo_animal int not null,
    fk_codigo_funcionario int not null,
    foreign key(fk_codigo_animal)references animal(codigo_animal),
    foreign key(fk_codigo_funcionario)references funcionario(codigo_funcionario)
);
