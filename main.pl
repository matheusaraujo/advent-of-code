#!/usr/bin/perl
use strict;
use warnings;

use Time::HiRes qw(time);
use feature 'say';

my $year = $ARGV[0];
my $day = $ARGV[1];

$year or die "Year is required";
$day or die "Day is required";

require "./$year/day$day/part1.pl";
require "./$year/day$day/part2.pl";

open(my $fh, '<', "$year/day$day/input.txt") or die "Could not open file 'input.txt' $!";

my @lines = <$fh>;
close $fh;

my $input = join('', @lines);

my $start_time1 = time();
my $result1 = part1($input);
my $end_time1 = time();
my $elapsed_time1 = $end_time1 - $start_time1;

my $start_time2 = time();
my $result2 = part2($input);
my $end_time2 = time();
my $elapsed_time2 = $end_time2 - $start_time2;

say "$year/day$day/part1.pl: $result1 - " . sprintf("%.4f", $elapsed_time1 * 1000) . "ms";
say "$year/day$day/part2.pl: $result2 - " . sprintf("%.4f", $elapsed_time2 * 1000) . "ms";