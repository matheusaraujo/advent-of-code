use strict;
use warnings;

sub parse_input {
    my @puzzle_input = @_;
    my ( @list1, @list2 );

    for my $line (@puzzle_input) {
        my ( $item1, $item2 ) = split /\s\s\s/sxm, $line;
        push @list1, $item1;
        push @list2, $item2;
    }

    @list1 = sort { $a <=> $b } @list1;
    @list2 = sort { $a <=> $b } @list2;

    return ( \@list1, \@list2 );
}

1;
