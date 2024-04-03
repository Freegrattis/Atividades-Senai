use escola;
select avg (idade_aluno) from estudante;
select truncate(avg (idade_aluno),2) from estudante;
select round(avg (idade_aluno),2) from estudante;
select min(idade_aluno) from estudante;
select max(idade_aluno) from estudante;

select nome_aluno, idade_aluno
	from estudante order by idade_aluno;
    
select *
	from estudante 
		where fk_turma=2 or fk_turma=3
			order by fk_turma;

select count(id_aluno), fk_turma
	from estudante 
		where fk_turma=2 or fk_turma=3
			group by fk_turma;
            
select *
	from estudante 
		inner join turma
        on estudante.fk_turma=turma.id_turma;
        
insert into estudante(nome_aluno,sobrenome_aluno,ano_ingresso_aluno,ano_egresso_aluno)
	values
		('joao','de jesus',50, 2020,2023); 

select E.nome_aluno, T.nome_turma
	from estudante as E
	left join turma as T
    on E.fk_turma = T.id_turma
    
union

select E.nome_aluno, T.nome_turma
	from estudante as E 
		right join turma as T
        on E. fk_turma=T.id_turma