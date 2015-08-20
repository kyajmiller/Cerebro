IF NOT EXISTS (SELECT * FROM master.dbo.syslogins WHERE loginname = N'SA\rafaeljgarcia')
CREATE LOGIN [SA\rafaeljgarcia] FROM WINDOWS
GO
CREATE USER [SA\rafaeljgarcia] FOR LOGIN [SA\rafaeljgarcia]
GO
