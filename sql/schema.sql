-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost
-- Généré le : ven. 18 sep. 2026 à 13:40
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
-- Base de données : `goncourt_test`
--

-- --------------------------------------------------------

--
-- Structure de la table `editor`
--

CREATE TABLE `editor` (
  `id_editor` int(11) NOT NULL,
  `name_editor` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `goncourt`
--

CREATE TABLE `goncourt` (
  `id_year` smallint(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `jury`
--

CREATE TABLE `jury` (
  `id_jury` int(11) NOT NULL,
  `id_author` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `main_character`
--

CREATE TABLE `main_character` (
  `id_main_character` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `id_novel` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `novel`
--

CREATE TABLE `novel` (
  `id_novel` int(11) NOT NULL,
  `title` varchar(50) DEFAULT NULL,
  `summary` text DEFAULT NULL,
  `editor` varchar(50) DEFAULT NULL,
  `publication_date` date DEFAULT NULL,
  `number_of_pages` smallint(6) DEFAULT NULL,
  `ISBN` decimal(13,0) DEFAULT NULL,
  `publisher_price` decimal(7,2) DEFAULT NULL,
  `id_person` int(11) NOT NULL,
  `id_editor` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `person`
--

CREATE TABLE `person` (
  `id_person` int(11) NOT NULL,
  `lastname` varchar(50) DEFAULT NULL,
  `firstname` varchar(50) DEFAULT NULL,
  `biography` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `roster`
--

CREATE TABLE `roster` (
  `id_year` smallint(6) NOT NULL,
  `id_jury` int(11) NOT NULL,
  `is_president` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `round`
--

CREATE TABLE `round` (
  `id_round` int(11) NOT NULL,
  `date_` date DEFAULT NULL,
  `id_year` smallint(6) NOT NULL,
  `id_round_parent` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `step`
--

CREATE TABLE `step` (
  `id_novel` int(11) NOT NULL,
  `id_round` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `vote`
--

CREATE TABLE `vote` (
  `id_vote` int(11) NOT NULL,
  `number_of_vote` smallint(6) DEFAULT NULL,
  `id_novel` int(11) NOT NULL,
  `id_year` smallint(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `editor`
--
ALTER TABLE `editor`
  ADD PRIMARY KEY (`id_editor`);

--
-- Index pour la table `goncourt`
--
ALTER TABLE `goncourt`
  ADD PRIMARY KEY (`id_year`);

--
-- Index pour la table `jury`
--
ALTER TABLE `jury`
  ADD PRIMARY KEY (`id_jury`),
  ADD UNIQUE KEY `id_author` (`id_author`);

--
-- Index pour la table `main_character`
--
ALTER TABLE `main_character`
  ADD PRIMARY KEY (`id_main_character`),
  ADD KEY `id_novel` (`id_novel`);

--
-- Index pour la table `novel`
--
ALTER TABLE `novel`
  ADD PRIMARY KEY (`id_novel`),
  ADD KEY `id_author` (`id_person`);

--
-- Index pour la table `person`
--
ALTER TABLE `person`
  ADD PRIMARY KEY (`id_person`);

--
-- Index pour la table `roster`
--
ALTER TABLE `roster`
  ADD PRIMARY KEY (`id_year`,`id_jury`),
  ADD KEY `id_jury` (`id_jury`);

--
-- Index pour la table `round`
--
ALTER TABLE `round`
  ADD PRIMARY KEY (`id_round`),
  ADD KEY `id_year` (`id_year`),
  ADD KEY `fk_round_parent` (`id_round_parent`);

--
-- Index pour la table `step`
--
ALTER TABLE `step`
  ADD PRIMARY KEY (`id_novel`,`id_round`),
  ADD KEY `id_round` (`id_round`);

--
-- Index pour la table `vote`
--
ALTER TABLE `vote`
  ADD PRIMARY KEY (`id_vote`),
  ADD UNIQUE KEY `id_novel` (`id_novel`),
  ADD KEY `id_year` (`id_year`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `editor`
--
ALTER TABLE `editor`
  MODIFY `id_editor` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `jury`
--
ALTER TABLE `jury`
  MODIFY `id_jury` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `main_character`
--
ALTER TABLE `main_character`
  MODIFY `id_main_character` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `novel`
--
ALTER TABLE `novel`
  MODIFY `id_novel` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `person`
--
ALTER TABLE `person`
  MODIFY `id_person` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `round`
--
ALTER TABLE `round`
  MODIFY `id_round` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `vote`
--
ALTER TABLE `vote`
  MODIFY `id_vote` int(11) NOT NULL AUTO_INCREMENT;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `jury`
--
ALTER TABLE `jury`
  ADD CONSTRAINT `jury_ibfk_1` FOREIGN KEY (`id_author`) REFERENCES `person` (`id_person`);

--
-- Contraintes pour la table `main_character`
--
ALTER TABLE `main_character`
  ADD CONSTRAINT `main_character_ibfk_1` FOREIGN KEY (`id_novel`) REFERENCES `novel` (`id_novel`);

--
-- Contraintes pour la table `novel`
--
ALTER TABLE `novel`
  ADD CONSTRAINT `novel_ibfk_1` FOREIGN KEY (`id_person`) REFERENCES `person` (`id_person`),
  ADD CONSTRAINT `novel_ibfk_2` FOREIGN KEY (`id_editor`) REFERENCES `editor` (`id_editor`);
--
-- Contraintes pour la table `roster`
--
ALTER TABLE `roster`
  ADD CONSTRAINT `roster_ibfk_1` FOREIGN KEY (`id_year`) REFERENCES `goncourt` (`id_year`),
  ADD CONSTRAINT `roster_ibfk_2` FOREIGN KEY (`id_jury`) REFERENCES `jury` (`id_jury`);

--
-- Contraintes pour la table `round`
--
ALTER TABLE `round`
  ADD CONSTRAINT `fk_round_parent` FOREIGN KEY (`id_round_parent`) REFERENCES `round` (`id_round`),
  ADD CONSTRAINT `round_ibfk_1` FOREIGN KEY (`id_year`) REFERENCES `goncourt` (`id_year`);

--
-- Contraintes pour la table `step`
--
ALTER TABLE `step`
  ADD CONSTRAINT `step_ibfk_1` FOREIGN KEY (`id_novel`) REFERENCES `novel` (`id_novel`),
  ADD CONSTRAINT `step_ibfk_2` FOREIGN KEY (`id_round`) REFERENCES `round` (`id_round`);

--
-- Contraintes pour la table `vote`
--
ALTER TABLE `vote`
  ADD CONSTRAINT `vote_ibfk_1` FOREIGN KEY (`id_novel`) REFERENCES `novel` (`id_novel`),
  ADD CONSTRAINT `vote_ibfk_2` FOREIGN KEY (`id_year`) REFERENCES `goncourt` (`id_year`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
