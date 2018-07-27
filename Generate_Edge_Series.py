from class_Sequence_Block_Rearrangments import EdgeSeries
from class_Sequence_Block_Rearrangments import WriteArrayToTextFile

if __name__ == "__main__":

    filenameB = '/home/18969577/Documents/Genolve/Shuffling/Sequence_block_rearrangements/GenomeB_names_positions'
    generate_edge_list = EdgeSeries()
    path, *remainder = filenameB.rpartition('/')
    output_filename = path + '/' + 'GenomeB_edge_list' + '.txt'
    edge_list = generate_edge_list.GenerateEdgesSeries(filenameB)
    output_file = WriteArrayToTextFile()
    output_file.WriteToTxt(edge_list, output_filename)

    print('Permutation series of edges for Genome B written to ', output_filename)