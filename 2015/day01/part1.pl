use strict;
use warnings;

sub part1 {
    my @puzzle_input = @_;
    my $result       = 0;

    $result =
      ( ( $puzzle_input[0] =~ tr/(// ) ) - ( $puzzle_input[0] =~ tr/)// );

    return $result;
}

1;
