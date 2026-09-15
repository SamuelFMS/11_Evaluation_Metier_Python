-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost
-- Généré le : mar. 15 sep. 2026 à 09:19
-- Version du serveur : 11.7.1-MariaDB
-- Version de PHP : 8.5.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `goncourt`
--

--
-- Déchargement des données de la table `goncourt`
--

INSERT INTO `goncourt` (`id_year`) VALUES
(2026);

--
-- Déchargement des données de la table `novel`
--

INSERT INTO `novel` (`id_novel`, `title`, `summary`, `editor`, `publication_date`, `number_of_pages`, `ISBN`, `publisher_price`, `id_person`) VALUES
(1, 'Minotaure', 'À vingt-trois ans, un jeune homme part à la rencon', 'Albin Michel', '2026-08-19', 256, 9782226511874, 20.90, 1),
(2, 'Faire la peau', 'Une narratrice de trente ans revient sur une enfan', 'P.O.L', '2026-08-20', 288, 9782818063583, 21.00, 2),
(3, 'Chronique d\'un royaume perdu', 'Sur l\'île Maurice, plusieurs générations vivent da', 'Grasset', '2026-08-19', 464, 9782246846949, 24.00, 3),
(4, 'Le Fabuleux Piano', 'Sonia Devillers enquête sur un piano à queue volé ', 'Robert Laffont', '2026-08-27', 288, 9782221286807, 21.00, 4),
(5, 'Nous aussi', 'Les enfants d\'une famille parisienne privilégiée g', 'Actes Sud', '2026-08-19', 240, 9782330225575, 20.00, 5),
(6, 'Joseph dans la nuit', 'Alors qu\'il voyage vers l\'Inde, Olivier Grondeau e', 'L\'Iconoclaste', '2026-08-20', 256, 9782378805975, 19.90, 6),
(7, 'La solitude des professeurs est infinie', 'Jean Deichel, jeune professeur de français, effect', 'Gallimard', '2026-08-20', 320, 9782073161925, 21.50, 7),
(8, 'Je', 'En Jamaïque en 1831, Antoinette Cosway s\'éprend d\'', 'Gallimard', '2026-08-20', 256, 9782073099945, 21.00, 8),
(9, 'L\'inconnue du quai de Javel', 'En 1949, Louise Cansot est retrouvée morte quai de', 'Flammarion', '2026-08-12', 528, 9782080490896, 23.00, 9),
(10, 'Une forêt', 'En 1947, dans une Allemagne dévastée, le capitaine', 'Albin Michel', '2026-01-02', 112, 9782226499523, 16.90, 10),
(11, 'N\'efface pas mes cercles', 'Après le suicide d\'une femme en 1980, la narratric', 'Verdier', '2026-08-20', 160, 9782378562953, 19.50, 11),
(12, 'Choses que je croyais perdues', 'Après une séparation, une jeune femme prépare son ', 'Gallimard', '2026-08-20', 176, 9782073162854, 19.00, 12),
(13, 'C\'était ça ou mourir', 'Après avoir fui la violence en Haïti, Jonas Dorléo', 'Grasset', '2026-08-19', 272, 9782246847069, 21.50, 13),
(14, 'De l\'autre côté du lac', 'Près d\'un lac de haute montagne bordant une réserv', 'Minuit', '2026-08-27', 288, 9782707358233, 22.00, 14),
(15, 'La Guerre éternelle', 'À partir de la guerre de Troie et d\'un voyage en T', 'Gallimard', '2026-08-20', 224, 9782073121349, 20.00, 15),
(16, 'Bataille au procès', 'En 1956, Georges Bataille témoigne au procès de Je', 'Maurice Nadeau', '2026-08-21', 146, 9782862316857, 19.00, 16);

--
-- Déchargement des données de la table `person`
--

INSERT INTO `person` (`id_person`, `lastname`, `firstname`, `biography`) VALUES
(1, 'BERGMANN', 'Boris', NULL),
(2, 'CHENNEVIÈRE', 'Louise', NULL),
(3, 'DEVI', 'Ananda', NULL),
(4, 'DEVILLERS', 'Sonia', NULL),
(5, 'GODARD', 'Anne', NULL),
(6, 'GRONDEAU', 'Olivier', NULL),
(7, 'HAENEL', 'Yannick', NULL),
(8, 'HASSAINE', 'Lilia', NULL),
(9, 'JAENADA', 'Philippe', NULL),
(10, 'JOUANNAIS', 'Jean-Yves', NULL),
(11, 'MARSANTES', 'Emma', NULL),
(12, 'MÉLOIS', 'Clémentine', NULL),
(13, 'ORÉLIEN', 'Thélyson', NULL),
(14, 'PRUDHOMME', 'Sylvain', NULL),
(15, 'ROLIN', 'Olivier', NULL),
(16, 'TRIGANO', 'Patrice', NULL);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
