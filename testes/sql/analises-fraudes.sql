-- Seleção de transações para enviar ao python

SELECT cliente_id, id, data_transacao_in FROM Transacoes_in 
GROUP BY cliente_id, id, data_transacao_in
ORDER BY  cliente_id, data_transacao_in


-- Analisando a tabela fraudes 

select * from Fraudes

-- Verificando os clientes que cometeram fraudes

select distinct c.id, c.nome from Clientes as c
inner join Transacoes_in as t 
on c.id = t.cliente_id
inner join Fraudes as f
on f.id_transacao = t.id 

--total de clientes in 13

select distinct c.id, c.nome from Clientes as c
inner join Transacoes_out as t 
on c.id = t.cliente_id
inner join Fraudes as f
on f.id_transacao = t.id 

-- total de clientes out 5

