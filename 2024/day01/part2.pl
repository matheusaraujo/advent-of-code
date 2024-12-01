#!/usr/bin/perl
use strict;
use warnings;

sub part2 {
    my @input  = @_;
    my $result = 0;
    my @list1;
    my @list2;

    for my $line (@input) {
        my @l = split /\s\s\s/sxm, $line;
        push @list1, $l[0];
        push @list2, $l[1];
    }

    foreach my $n1 (@list1) {
        my $appears = grep { $_ == $n1 } @list2;
        $result += $n1 * $appears;
    }

    return $result;
}

1;

