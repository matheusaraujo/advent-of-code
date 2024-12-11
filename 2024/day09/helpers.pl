use strict;
use warnings;

sub map_input_to_memory {
    my @puzzle_input = @_;
    my @memory       = ();

    my ( $is_file, $file_id, $left_pointer ) = ( 1, 0, 0 );

    foreach my $char ( split //sm, $puzzle_input[0] ) {
        my $id = $is_file ? $file_id : q{.};
        for ( 1 .. $char ) {
            $memory[ $left_pointer++ ] = $id;
        }
        $file_id += $is_file ? 1 : 0;
        $is_file = !$is_file;
    }

    return ( $file_id - 1, @memory );
}

sub calculate_checksum {
    my @memory = @_;
    my $result = 0;

    for my $i ( 0 .. $#memory ) {
        $result += $memory[$i] eq q{.} ? 0 : $i * $memory[$i];
    }

    return $result;
}

1;
