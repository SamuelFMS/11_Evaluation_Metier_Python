-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost
-- Généré le : ven. 18 sep. 2026 à 13:41
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
-- Déchargement des données de la table `editor`
--

INSERT INTO `editor` (`id_editor`, `name_editor`) VALUES
(1, 'Albin Michel'),
(3, 'P.O.L'),
(4, 'Grasset'),
(5, 'Robert Laffont'),
(6, 'Actes Sud'),
(7, 'L\'Iconoclaste'),
(8, 'Gallimard'),
(9, 'Flammarion'),
(10, 'Verdier'),
(11, 'Minuit'),
(12, 'Maurice Nadeau');

--
-- Déchargement des données de la table `goncourt`
--

INSERT INTO `goncourt` (`id_year`) VALUES
(2026);

--
-- Déchargement des données de la table `main_character`
--

INSERT INTO `main_character` (`id_main_character`, `name`, `id_novel`) VALUES
(1, 'Le narrateur', 1),
(2, 'Le père', 1),
(3, 'La narratrice', 2),
(4, 'La mère', 2),
(5, 'Sonia Devillers', 4),
(6, 'Olivier Grondeau', 6),
(7, 'Jean Deichel', 7),
(8, 'Antoinette Cosway', 8),
(9, 'Edward Rochester', 8),
(10, 'Louise Cansot', 9),
(11, 'Philippe Jaenada', 9),
(12, 'Inspecteur Ferrière', 9),
(13, 'Jacob Michael Lenz', 10),
(14, 'La narratrice', 11),
(15, 'La femme qui se suicide', 11),
(16, 'La narratrice', 12),
(17, 'Jonas Dorléon', 13),
(18, 'La photographe', 14),
(19, 'Olivier Rolin', 15),
(20, 'Georges Bataille', 16),
(21, 'Jean-Jacques Pauvert', 16);

--
-- Déchargement des données de la table `novel`
--

INSERT INTO `novel` (`id_novel`, `title`, `summary`, `publication_date`, `number_of_pages`, `ISBN`, `publisher_price`, `id_person`, `id_editor`) VALUES
(1, 'Minotaure', 'À vingt-trois ans, un jeune homme part à la rencontre de son père, qu\'il n\'a jamais connu. À travers cette quête intime, il revient sur son histoire familiale, son besoin d\'être aimé et sa manière de se construire malgré l\'absence paternelle.', '2026-08-19', 256, 9782226511874, 20.90, 1, 1),
(2, 'Faire la peau', 'Une narratrice de trente ans revient sur une enfance marquée par l\'emprise maternelle. Elle cherche à rompre avec une lignée de femmes où la violence se transmet de génération en génération et tente, par l\'écriture, de s\'émanciper de cette relation.', '2026-08-20', 288, 9782818063583, 21.00, 2, 3),
(3, 'Chronique d\'un royaume perdu', 'Sur l\'île Maurice, cinq enfants issus d\'une plantation fondent le Bouchon, un royaume isolé où réel et fantastique se confondent. Sur quatre générations, leurs descendants traversent passions, violences et bouleversements de l\'Histoire.', '2026-08-19', 464, 9782246846949, 24.00, 3, 4),
(4, 'Le Fabuleux Piano', 'Sonia Devillers enquête sur un piano à queue volé à une famille juive par les nazis en 1943. Sa recherche fait ressurgir l\'histoire des pianos pillés sous l\'Occupation, celle de la famille Enoch et les souvenirs de sa propre famille.', '2026-08-27', 288, 9782221286807, 21.00, 4, 5),
(5, 'Nous aussi', 'Les membres d\'une grande famille parisienne privilégiée vivent dans un univers où le groupe semble plus important que les individus. Mais lorsqu\'une fissure apparaît dans cette unité familiale, les certitudes et les liens qui les unissent commencent à vaciller.', '2026-08-19', 240, 9782330225575, 20.00, 5, 6),
(6, 'Joseph dans la nuit', 'Alors qu\'il traverse l\'Iran pour rejoindre l\'Inde, Olivier Grondeau est arrêté à Chiraz pendant le mouvement Femme, Vie, Liberté. Accusé d\'espionnage, il découvre la prison et tente de préserver sa liberté intérieure grâce à la poésie et à l\'imaginaire.', '2026-08-20', 256, 9782378805975, 19.90, 6, 7),
(7, 'La solitude des professeurs est infinie', 'Jean Deichel, jeune professeur de français, effectue son année de stage dans un collège difficile de la banlieue parisienne. Entre désillusions, rencontres avec ses élèves et aspirations littéraires, il découvre la réalité du métier d\'enseignant.', '2026-08-20', 320, 9782073161925, 21.50, 7, 8),
(8, 'Je', 'En Jamaïque en 1831, Antoinette Cosway s\'éprend d\'Edward Rochester, un Anglais fascinant et mystérieux. Leur relation devient progressivement destructrice. Des années plus tard, Antoinette tente de reprendre possession de son histoire et de sa propre voix.', '2026-08-20', 256, 9782073099945, 21.00, 8, 8),
(9, 'L\'inconnue du quai de Javel', 'En septembre 1949, Louise Cansot, modèle très demandé par les peintres de Montparnasse, est retrouvée morte quai de Javel à Paris. L\'affaire reste irrésolue. Soixante-quinze ans plus tard, Philippe Jaenada reprend le dossier et mène sa propre enquête.', '2026-08-12', 528, 9782080490896, 23.00, 9, 9),
(10, 'Une forêt', 'En 1947, dans une Allemagne dévastée, le capitaine américain Jacob Michael Lenz doit examiner une affaire étrange : des oiseaux d\'une forêt continuent de chanter des hymnes nazis. Cette mission absurde devient une réflexion sur la guerre, la mémoire et la culpabilité.', '2026-01-02', 112, 9782226499523, 16.90, 10, 1),
(11, 'N\'efface pas mes cercles', 'En 1980, une femme se suicide dans un appartement cossu. En explorant son histoire familiale, la narratrice remonte jusqu\'aux années cinquante et tente de comprendre ce drame, sur fond de patriarcat, de guerre, de colonisation et d\'injonctions sociales.', '2026-08-20', 160, 9782378562953, 19.50, 11, 10),
(12, 'Choses que je croyais perdues', 'Après une séparation, une jeune femme prépare son déménagement. Chaque objet qu\'elle range fait surgir des souvenirs de sa vie passée et de son histoire d\'amour. Les objets ordinaires deviennent ainsi les témoins des désirs, des pertes et des moments vécus.', '2026-08-20', 176, 9782073162854, 19.00, 12, 8),
(13, 'C\'était ça ou mourir', 'Après l\'embrasement de son quartier à Port-au-Prince, Jonas Dorléon quitte Haïti avec quelques affaires. De la République dominicaine au Mexique, il traverse plusieurs pays et affronte les dangers de l\'exil dans l\'espoir de rejoindre sa famille au Canada.', '2026-08-19', 272, 9782246847069, 21.50, 13, 4),
(14, 'De l\'autre côté du lac', 'Près d\'un lac de haute montagne bordant une réserve interdite aux humains, une photographe remarque quelque chose que les autres chercheurs ne voient pas. Des signes étranges apparaissent et un corps est découvert. Quelques mois plus tard, la photographe disparaît à son tour.', '2026-08-27', 288, 9782707358233, 22.00, 14, 11),
(15, 'La Guerre éternelle', 'À partir d\'un voyage sur les terres de l\'ancienne Troie, Olivier Rolin explore la destruction des villes et la permanence de la guerre à travers les siècles. L\'Iliade et la chute de Troie deviennent le point de départ d\'une réflexion sur les conflits jusqu\'à notre époque.', '2026-08-20', 224, 9782073121349, 20.00, 15, 8),
(16, 'Bataille au procès', 'En 1956, Georges Bataille témoigne au procès de Jean-Jacques Pauvert, poursuivi pour avoir publié les œuvres de Sade. L\'audience fait ressurgir chez Bataille des souvenirs de son enfance, de ses expériences et de ses réflexions sur la littérature, l\'érotisme, le sacré et la mort.', '2026-08-21', 146, 9782862316857, 19.00, 16, 12);

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

--
-- Déchargement des données de la table `round`
--

INSERT INTO `round` (`id_round`, `date_`, `id_year`, `id_round_parent`) VALUES
(1, NULL, 2026, NULL),
(2, NULL, 2026, 1),
(3, NULL, 2026, 2);

--
-- Déchargement des données de la table `step`
--

INSERT INTO `step` (`id_novel`, `id_round`) VALUES
(2, 1),
(3, 1),
(4, 1),
(5, 1),
(6, 1),
(7, 1),
(8, 1),
(9, 1),
(10, 1),
(11, 1),
(12, 1),
(13, 1),
(14, 1),
(15, 1),
(16, 1),
(2, 2),
(3, 2),
(4, 2),
(5, 2),
(6, 2),
(7, 2),
(8, 2),
(2, 3),
(3, 3),
(5, 3);

--
-- Déchargement des données de la table `vote`
--

INSERT INTO `vote` (`id_vote`, `number_of_vote`, `id_novel`, `id_year`) VALUES
(22, 7, 2, 2026),
(23, 3, 3, 2026),
(40, 0, 5, 2026);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
