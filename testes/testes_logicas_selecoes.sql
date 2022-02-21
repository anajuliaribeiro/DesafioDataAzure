-- como organizar as transações pelos clientes select cliente_id, id, data  from transaction_in group by cliente_id, id, dataorder by  cliente_id, dataselect  cliente_id, id, data from transaction_outgroup by cliente_id, id, dataorder by cliente_id, data

-- como comparar as datas para localizar as fraudes 

select cliente_id, id, data from transaction_out
where cliente_id = 671group by cliente_id, id, dataorder by cliente_id, data-- TESTE COMPARACAODECLARE @A DATETIME = '2022-01-03 12:22:44', @B DATETIME = '2022-01-03 12:25:04';
IF @A - @B <= 120
BEGIN
PRINT @A;
PRINT 'ele está fraudado';
PRINT @B;
END
ELSE
BEGIN
PRINT @A;
PRINT 'não é fraude';
PRINT @B;
END
PRINT 'CONTINUAÇÃO DO CÓDIGO'