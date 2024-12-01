#!/usr/bin/perl
use strict;
use warnings;

sub part1 {
    my @input  = @_;
    my $result = 0;
    my @list1;
    my @list2;

    for my $line (@input) {
        my @l = split /\s\s\s/sxm, $line;
        push @list1, $l[0];
        push @list2, $l[1];
    }

    @list1 = sort { $a <=> $b } @list1;
    @list2 = sort { $a <=> $b } @list2;

    foreach my $i ( 0 .. $#list1 ) {
        $result += abs $list1[$i] - $list2[$i];
    }

    return $result;
}

1;
