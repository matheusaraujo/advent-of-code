#!/usr/bin/perl
use strict;
use warnings;
use Carp;

my ( $year, $day, $part ) = @ARGV;
my $solution_path = "./$year/day$day/$part.pl";
my $helpers_path  = "./$year/day$day/helpers.pl";
my $func;

if ( -e $helpers_path ) {
    eval {
        do $helpers_path;
        1;
    } or croak "Could not load helpers file '$helpers_path': $@ $!";
}

eval {
    do $solution_path;
    $func = \&{$part};
    1;
} or croak "Could not load solution script '$solution_path': $@ $!";

sub main {
    my @input_data = <STDIN>;
    print $func->(@input_data);
}

main();
