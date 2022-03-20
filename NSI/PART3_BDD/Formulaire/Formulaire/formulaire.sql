CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL,`name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `subject` varchar(200) NOT NULL,
  `message` varchar(500) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

ALTER TABLE `users` ADD PRIMARY KEY (`id`);
ALTER TABLE `users`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;