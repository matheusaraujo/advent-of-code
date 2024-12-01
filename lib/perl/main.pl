#!/usr/bin/perl
use strict;
use warnings;
use Carp;

my ( $year, $day, $part ) = @ARGV;
my $solution_path = "./$year/day$day/$part.pl";
my $helpers_path  = "./$year/day$day/helpers.pl";
my $func          = \&{$part};

if ( -e $helpers_path ) {
    do $helpers_path or croak "Could not load helpers: $!";
}
do $solution_path or croak "Could not load script '$solution_path': $!";

sub main {
    my @input_data = <STDIN>;
    print $func->(@input_data);
}

main();
