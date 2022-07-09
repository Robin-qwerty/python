-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jul 09, 2022 at 06:46 PM
-- Server version: 10.6.8-MariaDB
-- PHP Version: 8.1.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pythonDB`
--

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `id` int(11) NOT NULL,
  `url` varchar(111) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(55) COLLATE utf8mb4_unicode_ci NOT NULL,
  `stock` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`id`, `url`, `name`, `stock`) VALUES
(28, 'https://droneshop.nl/radiomaster-tx16s', 'RADIOMASTER TX16S', 0),
(30, 'https://droneshop.nl/geprc-cinelog35-analog-4s-pnp', 'GEPRC CINELOG35 - ANALOG - 4S - PNP', 1),
(31, 'https://droneshop.nl/dji-mini-2', 'DJI Mini 2', 1);

-- --------------------------------------------------------

--
-- Table structure for table `product_track`
--

CREATE TABLE `product_track` (
  `id` int(11) NOT NULL,
  `product` int(11) NOT NULL,
  `date` date NOT NULL,
  `price` double(9,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `product_track`
--

INSERT INTO `product_track` (`id`, `product`, `date`, `price`) VALUES
(1, 28, '2022-07-09', 198.00),
(3, 30, '2022-07-09', 319.00),
(4, 31, '2022-07-09', 449.00);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id` (`id`);

--
-- Indexes for table `product_track`
--
ALTER TABLE `product_track`
  ADD PRIMARY KEY (`id`),
  ADD KEY `product` (`product`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `product_track`
--
ALTER TABLE `product_track`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `product_track`
--
ALTER TABLE `product_track`
  ADD CONSTRAINT `product_track_ibfk_1` FOREIGN KEY (`product`) REFERENCES `product` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
