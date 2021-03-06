USE [master]
GO
/****** Object:  Database [KruskalWallisDB]    Script Date: 20-03-2022 13:35:17 ******/
CREATE DATABASE [KruskalWallisDB]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'KruskalWallisDB', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\KruskalWallisDB.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'KruskalWallisDB_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\KruskalWallisDB_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO
ALTER DATABASE [KruskalWallisDB] SET COMPATIBILITY_LEVEL = 150
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [KruskalWallisDB].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [KruskalWallisDB] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [KruskalWallisDB] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [KruskalWallisDB] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [KruskalWallisDB] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [KruskalWallisDB] SET ARITHABORT OFF 
GO
ALTER DATABASE [KruskalWallisDB] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [KruskalWallisDB] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [KruskalWallisDB] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [KruskalWallisDB] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [KruskalWallisDB] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [KruskalWallisDB] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [KruskalWallisDB] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [KruskalWallisDB] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [KruskalWallisDB] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [KruskalWallisDB] SET  DISABLE_BROKER 
GO
ALTER DATABASE [KruskalWallisDB] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [KruskalWallisDB] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [KruskalWallisDB] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [KruskalWallisDB] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [KruskalWallisDB] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [KruskalWallisDB] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [KruskalWallisDB] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [KruskalWallisDB] SET RECOVERY FULL 
GO
ALTER DATABASE [KruskalWallisDB] SET  MULTI_USER 
GO
ALTER DATABASE [KruskalWallisDB] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [KruskalWallisDB] SET DB_CHAINING OFF 
GO
ALTER DATABASE [KruskalWallisDB] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [KruskalWallisDB] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [KruskalWallisDB] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [KruskalWallisDB] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
EXEC sys.sp_db_vardecimal_storage_format N'KruskalWallisDB', N'ON'
GO
ALTER DATABASE [KruskalWallisDB] SET QUERY_STORE = OFF
GO
USE [KruskalWallisDB]
GO
/****** Object:  Table [dbo].[Table_1]    Script Date: 20-03-2022 13:35:17 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Table_1](
	[SNo] [int] NULL,
	[NoExercise] [int] NULL,
	[Exercise_20M] [int] NULL,
	[Exercise_40M] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Table_2]    Script Date: 20-03-2022 13:35:17 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Table_2](
	[SNo] [int] NULL,
	[NoExercise] [decimal](18, 2) NULL,
	[Exercise_20M] [decimal](18, 2) NULL,
	[Exercise_40M] [decimal](18, 2) NULL
) ON [PRIMARY]
GO
INSERT [dbo].[Table_1] ([SNo], [NoExercise], [Exercise_20M], [Exercise_40M]) VALUES (1, 23, 22, 59)
INSERT [dbo].[Table_1] ([SNo], [NoExercise], [Exercise_20M], [Exercise_40M]) VALUES (2, 26, 27, 66)
INSERT [dbo].[Table_1] ([SNo], [NoExercise], [Exercise_20M], [Exercise_40M]) VALUES (3, 51, 39, 38)
INSERT [dbo].[Table_1] ([SNo], [NoExercise], [Exercise_20M], [Exercise_40M]) VALUES (4, 49, 29, 49)
INSERT [dbo].[Table_1] ([SNo], [NoExercise], [Exercise_20M], [Exercise_40M]) VALUES (5, 58, 46, 56)
INSERT [dbo].[Table_1] ([SNo], [NoExercise], [Exercise_20M], [Exercise_40M]) VALUES (6, 37, 48, 60)
INSERT [dbo].[Table_1] ([SNo], [NoExercise], [Exercise_20M], [Exercise_40M]) VALUES (7, 29, 49, 56)
INSERT [dbo].[Table_1] ([SNo], [NoExercise], [Exercise_20M], [Exercise_40M]) VALUES (8, 44, 65, 62)
GO
INSERT [dbo].[Table_2] ([SNo], [NoExercise], [Exercise_20M], [Exercise_40M]) VALUES (1, CAST(2.00 AS Decimal(18, 2)), CAST(1.00 AS Decimal(18, 2)), CAST(20.00 AS Decimal(18, 2)))
INSERT [dbo].[Table_2] ([SNo], [NoExercise], [Exercise_20M], [Exercise_40M]) VALUES (2, CAST(3.00 AS Decimal(18, 2)), CAST(4.00 AS Decimal(18, 2)), CAST(24.00 AS Decimal(18, 2)))
INSERT [dbo].[Table_2] ([SNo], [NoExercise], [Exercise_20M], [Exercise_40M]) VALUES (3, CAST(16.00 AS Decimal(18, 2)), CAST(9.00 AS Decimal(18, 2)), CAST(8.00 AS Decimal(18, 2)))
INSERT [dbo].[Table_2] ([SNo], [NoExercise], [Exercise_20M], [Exercise_40M]) VALUES (4, CAST(14.00 AS Decimal(18, 2)), CAST(5.50 AS Decimal(18, 2)), CAST(14.00 AS Decimal(18, 2)))
INSERT [dbo].[Table_2] ([SNo], [NoExercise], [Exercise_20M], [Exercise_40M]) VALUES (5, CAST(19.00 AS Decimal(18, 2)), CAST(11.00 AS Decimal(18, 2)), CAST(17.50 AS Decimal(18, 2)))
INSERT [dbo].[Table_2] ([SNo], [NoExercise], [Exercise_20M], [Exercise_40M]) VALUES (6, CAST(7.00 AS Decimal(18, 2)), CAST(12.00 AS Decimal(18, 2)), CAST(21.00 AS Decimal(18, 2)))
INSERT [dbo].[Table_2] ([SNo], [NoExercise], [Exercise_20M], [Exercise_40M]) VALUES (7, CAST(5.50 AS Decimal(18, 2)), CAST(14.00 AS Decimal(18, 2)), CAST(17.50 AS Decimal(18, 2)))
INSERT [dbo].[Table_2] ([SNo], [NoExercise], [Exercise_20M], [Exercise_40M]) VALUES (8, CAST(10.00 AS Decimal(18, 2)), CAST(23.00 AS Decimal(18, 2)), CAST(22.00 AS Decimal(18, 2)))
GO
USE [master]
GO
ALTER DATABASE [KruskalWallisDB] SET  READ_WRITE 
GO
