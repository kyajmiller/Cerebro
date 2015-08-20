IF NOT EXISTS (SELECT * FROM master.dbo.syslogins WHERE loginname = N'EM\__su_service')
CREATE LOGIN [EM\__su_service] FROM WINDOWS
GO
CREATE USER [EM\__su_service] FOR LOGIN [EM\__su_service]
GO
