import tensorflow as tf
 
operations = set( ['Abort', 'Abs', 'AccumulateNV2', 'AccumulatorApplyGradient', 'AccumulatorNumAccumulated', 'AccumulatorSetGlobalStep', 'AccumulatorTakeGradient', 'Acos', 'Acosh', 'Add', 'AddManySparseToTensorsMap', 'AddN', 'AddSparseToTensorsMap', 'AddV2', 'AdjustContrast', 'AdjustContrastv2', 'AdjustHue', 'AdjustSaturation', 'All', 'AllCandidateSampler', 'AllToAll', 'Angle', 'AnonymousIterator', 'AnonymousIteratorV2', 'AnonymousMemoryCache', 'AnonymousMultiDeviceIterator', 'AnonymousRandomSeedGenerator', 'Any', 'ApplyAdaMax', 'ApplyAdadelta', 'ApplyAdagrad', 'ApplyAdagradDA', 'ApplyAdagradV2', 'ApplyAdam', 'ApplyAddSign', 'ApplyCenteredRMSProp', 'ApplyFtrl', 'ApplyFtrlV2', 'ApplyGradientDescent', 'ApplyMomentum', 'ApplyPowerSign', 'ApplyProximalAdagrad', 'ApplyProximalGradientDescent', 'ApplyRMSProp', 'ApproximateEqual', 'ArgMax', 'ArgMin', 'AsString', 'Asin', 'Asinh', 'Assert', 'AssertCardinalityDataset', 'AssertNextDataset', 'Assign', 'AssignAdd', 'AssignAddVariableOp', 'AssignSub', 'AssignSubVariableOp', 'AssignVariableOp', 'Atan', 'Atan2', 'Atanh', 'AudioSpectrogram', 'AudioSummary', 'AudioSummaryV2', 'AutoShardDataset', 'AvgPool', 'AvgPool3D', 'AvgPool3DGrad', 'AvgPoolGrad', 'Barrier', 'BarrierClose', 'BarrierIncompleteSize', 'BarrierInsertMany', 'BarrierReadySize', 'BarrierTakeMany', 'Batch', 'BatchCholesky', 'BatchCholeskyGrad', 'BatchDataset', 'BatchDatasetV2', 'BatchFFT', 'BatchFFT2D', 'BatchFFT3D', 'BatchFunction', 'BatchIFFT', 'BatchIFFT2D', 'BatchIFFT3D', 'BatchMatMul', 'BatchMatMulV2', 'BatchMatrixBandPart', 'BatchMatrixDeterminant', 'BatchMatrixDiag', 'BatchMatrixDiagPart', 'BatchMatrixInverse', 'BatchMatrixSetDiag', 'BatchMatrixSolve', 'BatchMatrixSolveLs', 'BatchMatrixTriangularSolve', 'BatchNormWithGlobalNormalization', 'BatchNormWithGlobalNormalizationGrad', 'BatchSelfAdjointEig', 'BatchSelfAdjointEigV2', 'BatchSvd', 'BatchToSpace', 'BatchToSpaceND', 'BesselI0e', 'BesselI1e', 'Betainc', 'BiasAdd', 'BiasAddGrad', 'BiasAddV1', 'Bincount', 'Bitcast', 'BitwiseAnd', 'BitwiseOr', 'BitwiseXor', 'BlockLSTM', 'BlockLSTMGrad', 'BlockLSTMGradV2', 'BlockLSTMV2', 'BoostedTreesAggregateStats', 'BoostedTreesBucketize', 'BoostedTreesCalculateBestFeatureSplit', 'BoostedTreesCalculateBestFeatureSplitV2', 'BoostedTreesCalculateBestGainsPerFeature', 'BoostedTreesCenterBias', 'BoostedTreesCreateEnsemble', 'BoostedTreesCreateQuantileStreamResource', 'BoostedTreesDeserializeEnsemble', 'BoostedTreesEnsembleResourceHandleOp', 'BoostedTreesExampleDebugOutputs', 'BoostedTreesFlushQuantileSummaries', 'BoostedTreesGetEnsembleStates', 'BoostedTreesMakeQuantileSummaries', 'BoostedTreesMakeStatsSummary', 'BoostedTreesPredict', 'BoostedTreesQuantileStreamResourceAddSummaries', 'BoostedTreesQuantileStreamResourceDeserialize', 'BoostedTreesQuantileStreamResourceFlush', 'BoostedTreesQuantileStreamResourceGetBucketBoundaries', 'BoostedTreesQuantileStreamResourceHandleOp', 'BoostedTreesSerializeEnsemble', 'BoostedTreesSparseAggregateStats', 'BoostedTreesSparseCalculateBestFeatureSplit', 'BoostedTreesTrainingPredict', 'BoostedTreesUpdateEnsemble', 'BoostedTreesUpdateEnsembleV2', 'BroadcastArgs', 'BroadcastGradientArgs', 'BroadcastTo', 'Bucketize', 'BytesProducedStatsDataset', 'CSRSparseMatrixComponents', 'CSRSparseMatrixToDense', 'CSRSparseMatrixToSparseTensor', 'CSVDataset', 'CTCBeamSearchDecoder', 'CTCGreedyDecoder', 'CTCLoss', 'CTCLossV2', 'CacheDataset', 'CacheDatasetV2', 'Case', 'Cast', 'Ceil', 'CheckNumerics', 'CheckNumericsV2', 'Cholesky', 'CholeskyGrad', 'ChooseFastestBranchDataset', 'ChooseFastestDataset', 'ClipByValue', 'CloseSummaryWriter', 'CollectiveBcastRecv', 'CollectiveBcastSend', 'CollectiveGather', 'CollectivePermute', 'CollectiveReduce', 'CombinedNonMaxSuppression', 'CompareAndBitpack', 'Complex', 'ComplexAbs', 'ComputeAccidentalHits', 'Concat', 'ConcatOffset', 'ConcatV2', 'ConcatenateDataset', 'ConditionalAccumulator', 'ConfigureDistributedTPU', 'ConfigureTPUEmbedding', 'Conj', 'ConjugateTranspose', 'Const', 'ConsumeMutexLock', 'ControlTrigger', 'Conv2D', 'Conv2DBackpropFilter', 'Conv2DBackpropInput', 'Conv3D', 'Conv3DBackpropFilter', 'Conv3DBackpropFilterV2', 'Conv3DBackpropInput', 'Conv3DBackpropInputV2', 'Copy', 'CopyHost', 'Cos', 'Cosh', 'CountUpTo', 'CreateSummaryDbWriter', 'CreateSummaryFileWriter', 'CropAndResize', 'CropAndResizeGradBoxes', 'CropAndResizeGradImage', 'Cross', 'CrossReplicaSum', 'CudnnRNN', 'CudnnRNNBackprop', 'CudnnRNNBackpropV2', 'CudnnRNNBackpropV3', 'CudnnRNNCanonicalToParams', 'CudnnRNNCanonicalToParamsV2', 'CudnnRNNParamsSize', 'CudnnRNNParamsToCanonical', 'CudnnRNNParamsToCanonicalV2', 'CudnnRNNV2', 'CudnnRNNV3', 'Cumprod', 'Cumsum', 'CumulativeLogsumexp', 'DataFormatDimMap', 'DataFormatVecPermute', 'DatasetCardinality', 'DatasetFromGraph', 'DatasetToGraph', 'DatasetToGraphV2', 'DatasetToSingleElement', 'DatasetToTFRecord', 'Dawsn', 'DebugGradientIdentity', 'DebugGradientRefIdentity', 'DebugIdentity', 'DebugIdentityV2', 'DebugNanCount', 'DebugNumericSummary', 'DebugNumericSummaryV2', 'DecodeAndCropJpeg', 'DecodeBase64', 'DecodeBmp', 'DecodeCSV', 'DecodeCompressed', 'DecodeGif', 'DecodeJSONExample', 'DecodeJpeg', 'DecodePaddedRaw', 'DecodePng', 'DecodeProtoV2', 'DecodeRaw', 'DecodeWav', 'DeepCopy', 'DeleteIterator', 'DeleteMemoryCache', 'DeleteMultiDeviceIterator', 'DeleteRandomSeedGenerator', 'DeleteSessionTensor', 'DenseToCSRSparseMatrix', 'DenseToDenseSetOperation', 'DenseToSparseBatchDataset', 'DenseToSparseSetOperation', 'DepthToSpace', 'DepthwiseConv2dNative', 'DepthwiseConv2dNativeBackpropFilter', 'DepthwiseConv2dNativeBackpropInput', 'Dequantize', 'DeserializeIterator', 'DeserializeManySparse', 'DeserializeSparse', 'DestroyResourceOp', 'DestroyTemporaryVariable', 'Diag', 'DiagPart', 'Digamma', 'Dilation2D', 'Dilation2DBackpropFilter', 'Dilation2DBackpropInput', 'DirectedInterleaveDataset', 'Div', 'DivNoNan', 'DrawBoundingBoxes', 'DrawBoundingBoxesV2', 'DummyMemoryCache', 'DynamicPartition', 'DynamicStitch', 'EagerPyFunc', 'EditDistance', 'Eig', 'Einsum', 'Elu', 'EluGrad', 'Empty', 'EmptyTensorList', 'EncodeBase64', 'EncodeJpeg', 'EncodeJpegVariableQuality', 'EncodePng', 'EncodeProto', 'EncodeWav', 'EnqueueTPUEmbeddingIntegerBatch', 'EnqueueTPUEmbeddingSparseBatch', 'EnqueueTPUEmbeddingSparseTensorBatch', 'EnsureShape', 'Enter', 'Equal', 'Erf', 'Erfc', 'Erfinv', 'EuclideanNorm', 'Exit', 'Exp', 'ExpandDims', 'ExperimentalAssertNextDataset', 'ExperimentalAutoShardDataset', 'ExperimentalBytesProducedStatsDataset', 'ExperimentalCSVDataset', 'ExperimentalChooseFastestDataset', 'ExperimentalDatasetCardinality', 'ExperimentalDatasetToTFRecord', 'ExperimentalDenseToSparseBatchDataset', 'ExperimentalDirectedInterleaveDataset', 'ExperimentalGroupByReducerDataset', 'ExperimentalGroupByWindowDataset', 'ExperimentalIgnoreErrorsDataset', 'ExperimentalIteratorGetDevice', 'ExperimentalLMDBDataset', 'ExperimentalLatencyStatsDataset', 'ExperimentalMapAndBatchDataset', 'ExperimentalMapDataset', 'ExperimentalMatchingFilesDataset', 'ExperimentalMaxIntraOpParallelismDataset', 'ExperimentalNonSerializableDataset', 'ExperimentalParallelInterleaveDataset', 'ExperimentalParseExampleDataset', 'ExperimentalPrivateThreadPoolDataset', 'ExperimentalRandomDataset', 'ExperimentalRebatchDataset', 'ExperimentalScanDataset', 'ExperimentalSetStatsAggregatorDataset', 'ExperimentalSleepDataset', 'ExperimentalSlidingWindowDataset', 'ExperimentalSqlDataset', 'ExperimentalStatsAggregatorHandle', 'ExperimentalStatsAggregatorSummary', 'ExperimentalTakeWhileDataset', 'ExperimentalThreadPoolDataset', 'ExperimentalThreadPoolHandle', 'ExperimentalUnbatchDataset', 'ExperimentalUniqueDataset', 'Expint', 'Expm1', 'ExtractGlimpse', 'ExtractImagePatches', 'ExtractJpegShape', 'ExtractVolumePatches', 'FFT', 'FFT2D', 'FFT3D', 'FIFOQueue', 'FIFOQueueV2', 'Fact', 'FakeParam', 'FakeQuantWithMinMaxArgs', 'FakeQuantWithMinMaxArgsGradient', 'FakeQuantWithMinMaxVars', 'FakeQuantWithMinMaxVarsGradient', 'FakeQuantWithMinMaxVarsPerChannel', 'FakeQuantWithMinMaxVarsPerChannelGradient', 'FakeQueue', 'Fill', 'FilterByLastComponentDataset', 'FilterDataset', 'Fingerprint', 'FixedLengthRecordDataset', 'FixedLengthRecordDatasetV2', 'FixedLengthRecordReader', 'FixedLengthRecordReaderV2', 'FixedUnigramCandidateSampler', 'FlatMapDataset', 'Floor', 'FloorDiv', 'FloorMod', 'FlushSummaryWriter', 'For', 'FractionalAvgPool', 'FractionalAvgPoolGrad', 'FractionalMaxPool', 'FractionalMaxPoolGrad', 'FresnelCos', 'FresnelSin', 'FusedBatchNorm', 'FusedBatchNormGrad', 'FusedBatchNormGradV2', 'FusedBatchNormGradV3', 'FusedBatchNormV2', 'FusedBatchNormV3', 'FusedPadConv2D', 'FusedResizeAndPadConv2D', 'GRUBlockCell', 'GRUBlockCellGrad', 'Gather', 'GatherNd', 'GatherV2', 'GenerateBoundingBoxProposals', 'GenerateVocabRemapping', 'GeneratorDataset', 'GetSessionHandle', 'GetSessionHandleV2', 'GetSessionTensor', 'Greater', 'GreaterEqual', 'GroupByReducerDataset', 'GroupByWindowDataset', 'GuaranteeConst', 'HSVToRGB', 'HashTable', 'HashTableV2', 'HistogramFixedWidth', 'HistogramSummary', 'IFFT', 'IFFT2D', 'IFFT3D', 'IRFFT', 'IRFFT2D', 'IRFFT3D', 'Identity', 'IdentityN', 'IdentityReader', 'IdentityReaderV2', 'If', 'Igamma', 'IgammaGradA', 'Igammac', 'IgnoreErrorsDataset', 'Imag', 'ImageProjectiveTransformV2', 'ImageSummary', 'ImmutableConst', 'ImportEvent', 'InTopK', 'InTopKV2', 'InfeedDequeue', 'InfeedDequeueTuple', 'InfeedEnqueue', 'InfeedEnqueuePrelinearizedBuffer', 'InfeedEnqueueTuple', 'InitializeTable', 'InitializeTableFromTextFile', 'InitializeTableFromTextFileV2', 'InitializeTableV2', 'InplaceAdd', 'InplaceSub', 'InplaceUpdate', 'InterleaveDataset', 'Inv', 'InvGrad', 'Invert', 'InvertPermutation', 'IsBoostedTreesEnsembleInitialized', 'IsBoostedTreesQuantileStreamResourceInitialized', 'IsFinite', 'IsInf', 'IsNan', 'IsVariableInitialized', 'Iterator', 'IteratorFromStringHandle', 'IteratorFromStringHandleV2', 'IteratorGetDevice', 'IteratorGetNext', 'IteratorGetNextAsOptional', 'IteratorGetNextSync', 'IteratorToStringHandle', 'IteratorV2', 'L2Loss', 'LMDBDataset', 'LMDBReader', 'LRN', 'LRNGrad', 'LSTMBlockCell', 'LSTMBlockCellGrad', 'LatencyStatsDataset', 'LeakyRelu', 'LeakyReluGrad', 'LearnedUnigramCandidateSampler', 'LeftShift', 'LegacyParallelInterleaveDatasetV2', 'Less', 'LessEqual', 'Lgamma', 'LinSpace', 'ListDiff', 'LoadAndRemapMatrix', 'LoadTPUEmbeddingADAMParameters', 'LoadTPUEmbeddingADAMParametersGradAccumDebug', 'LoadTPUEmbeddingAdadeltaParameters', 'LoadTPUEmbeddingAdadeltaParametersGradAccumDebug', 'LoadTPUEmbeddingAdagradParameters', 'LoadTPUEmbeddingAdagradParametersGradAccumDebug', 'LoadTPUEmbeddingCenteredRMSPropParameters', 'LoadTPUEmbeddingFTRLParameters', 'LoadTPUEmbeddingFTRLParametersGradAccumDebug', 'LoadTPUEmbeddingMDLAdagradLightParameters', 'LoadTPUEmbeddingMomentumParameters', 'LoadTPUEmbeddingMomentumParametersGradAccumDebug', 'LoadTPUEmbeddingProximalAdagradParameters', 'LoadTPUEmbeddingProximalAdagradParametersGradAccumDebug', 'LoadTPUEmbeddingRMSPropParameters', 'LoadTPUEmbeddingRMSPropParametersGradAccumDebug', 'LoadTPUEmbeddingStochasticGradientDescentParameters', 'Log', 'Log1p', 'LogMatrixDeterminant', 'LogSoftmax', 'LogUniformCandidateSampler', 'LogicalAnd', 'LogicalNot', 'LogicalOr', 'LookupTableExport', 'LookupTableExportV2', 'LookupTableFind', 'LookupTableFindV2', 'LookupTableImport', 'LookupTableImportV2', 'LookupTableInsert', 'LookupTableInsertV2', 'LookupTableRemoveV2', 'LookupTableSize', 'LookupTableSizeV2', 'LoopCond', 'LowerBound', 'Lu', 'MakeIterator', 'MapAndBatchDataset', 'MapClear', 'MapDataset', 'MapDefun', 'MapIncompleteSize', 'MapPeek', 'MapSize', 'MapStage', 'MapUnstage', 'MapUnstageNoKey', 'MatMul', 'MatchingFiles', 'MatchingFilesDataset', 'MatrixBandPart', 'MatrixDeterminant', 'MatrixDiag', 'MatrixDiagPart', 'MatrixDiagPartV2', 'MatrixDiagPartV3', 'MatrixDiagV2', 'MatrixDiagV3', 'MatrixExponential', 'MatrixInverse', 'MatrixLogarithm', 'MatrixSetDiag', 'MatrixSetDiagV2', 'MatrixSetDiagV3', 'MatrixSolve', 'MatrixSolveLs', 'MatrixSquareRoot', 'MatrixTriangularSolve', 'Max', 'MaxIntraOpParallelismDataset', 'MaxPool', 'MaxPool3D', 'MaxPool3DGrad', 'MaxPool3DGradGrad', 'MaxPoolGrad', 'MaxPoolGradGrad', 'MaxPoolGradGradV2', 'MaxPoolGradGradWithArgmax', 'MaxPoolGradV2', 'MaxPoolGradWithArgmax', 'MaxPoolV2', 'MaxPoolWithArgmax', 'Maximum', 'Mean', 'Merge', 'MergeSummary', 'MergeV2Checkpoints', 'Mfcc', 'Min', 'Minimum', 'MirrorPad', 'MirrorPadGrad', 'Mod', 'ModelDataset', 'Mul', 'MulNoNan', 'MultiDeviceIterator', 'MultiDeviceIteratorFromStringHandle', 'MultiDeviceIteratorGetNextFromShard', 'MultiDeviceIteratorInit', 'MultiDeviceIteratorToStringHandle', 'Multinomial', 'MutableDenseHashTable', 'MutableDenseHashTableV2', 'MutableHashTable', 'MutableHashTableOfTensors', 'MutableHashTableOfTensorsV2', 'MutableHashTableV2', 'MutexLock', 'MutexV2', 'NcclAllReduce', 'NcclBroadcast', 'NcclReduce', 'Ndtri', 'Neg', 'NextAfter', 'NextIteration', 'NoOp', 'NonDeterministicInts', 'NonMaxSuppression', 'NonMaxSuppressionV2', 'NonMaxSuppressionV3', 'NonMaxSuppressionV4', 'NonMaxSuppressionV5', 'NonMaxSuppressionWithOverlaps', 'NonSerializableDataset', 'NotEqual', 'NthElement', 'OneHot', 'OneShotIterator', 'OnesLike', 'OptimizeDataset', 'OptionalFromValue', 'OptionalGetValue', 'OptionalHasValue', 'OptionalNone', 'OrderedMapClear', 'OrderedMapIncompleteSize', 'OrderedMapPeek', 'OrderedMapSize', 'OrderedMapStage', 'OrderedMapUnstage', 'OrderedMapUnstageNoKey', 'OutfeedDequeue', 'OutfeedDequeueTuple', 'OutfeedEnqueue', 'OutfeedEnqueueTuple', 'Pack', 'Pad', 'PadV2', 'PaddedBatchDataset', 'PaddedBatchDatasetV2', 'PaddingFIFOQueue', 'PaddingFIFOQueueV2', 'ParallelConcat', 'ParallelDynamicStitch', 'ParallelInterleaveDataset', 'ParallelInterleaveDatasetV2', 'ParallelInterleaveDatasetV3', 'ParallelInterleaveDatasetV4', 'ParallelMapDataset', 'ParallelMapDatasetV2', 'ParameterizedTruncatedNormal', 'ParseExample', 'ParseExampleDataset', 'ParseExampleDatasetV2', 'ParseExampleV2', 'ParseSequenceExample', 'ParseSequenceExampleV2', 'ParseSingleExample', 'ParseSingleSequenceExample', 'ParseTensor', 'PartitionedCall', 'Placeholder', 'PlaceholderV2', 'PlaceholderWithDefault', 'Polygamma', 'PopulationCount', 'Pow', 'PrefetchDataset', 'Prelinearize', 'PrelinearizeTuple', 'PreventGradient', 'Print', 'PrintV2', 'PriorityQueue', 'PriorityQueueV2', 'PrivateThreadPoolDataset', 'Prod', 'PyFunc', 'PyFuncStateless', 'Qr', 'QuantizeAndDequantize', 'QuantizeAndDequantizeV2', 'QuantizeAndDequantizeV3', 'QuantizeDownAndShrinkRange', 'QuantizeV2', 'QuantizedAdd', 'QuantizedAvgPool', 'QuantizedBatchNormWithGlobalNormalization', 'QuantizedBiasAdd', 'QuantizedConcat', 'QuantizedConv2D', 'QuantizedConv2DAndRelu', 'QuantizedConv2DAndReluAndRequantize', 'QuantizedConv2DAndRequantize', 'QuantizedConv2DPerChannel', 'QuantizedConv2DWithBias', 'QuantizedConv2DWithBiasAndRelu', 'QuantizedConv2DWithBiasAndReluAndRequantize', 'QuantizedConv2DWithBiasAndRequantize', 'QuantizedConv2DWithBiasSignedSumAndReluAndRequantize', 'QuantizedConv2DWithBiasSumAndRelu', 'QuantizedConv2DWithBiasSumAndReluAndRequantize', 'QuantizedDepthwiseConv2D', 'QuantizedDepthwiseConv2DWithBias', 'QuantizedDepthwiseConv2DWithBiasAndRelu', 'QuantizedDepthwiseConv2DWithBiasAndReluAndRequantize', 'QuantizedInstanceNorm', 'QuantizedMatMul', 'QuantizedMatMulWithBias', 'QuantizedMatMulWithBiasAndDequantize', 'QuantizedMatMulWithBiasAndRelu', 'QuantizedMatMulWithBiasAndReluAndRequantize', 'QuantizedMatMulWithBiasAndRequantize', 'QuantizedMaxPool', 'QuantizedMul', 'QuantizedRelu', 'QuantizedRelu6', 'QuantizedReluX', 'QuantizedReshape', 'QuantizedResizeBilinear', 'QueueClose', 'QueueCloseV2', 'QueueDequeue', 'QueueDequeueMany', 'QueueDequeueManyV2', 'QueueDequeueUpTo', 'QueueDequeueUpToV2', 'QueueDequeueV2', 'QueueEnqueue', 'QueueEnqueueMany', 'QueueEnqueueManyV2', 'QueueEnqueueV2', 'QueueIsClosed', 'QueueIsClosedV2', 'QueueSize', 'QueueSizeV2', 'RFFT', 'RFFT2D', 'RFFT3D', 'RGBToHSV', 'RaggedGather', 'RaggedRange', 'RaggedTensorFromVariant', 'RaggedTensorToSparse', 'RaggedTensorToTensor', 'RaggedTensorToVariant', 'RandomCrop', 'RandomDataset', 'RandomGamma', 'RandomGammaGrad', 'RandomPoisson', 'RandomPoissonV2', 'RandomShuffle', 'RandomShuffleQueue', 'RandomShuffleQueueV2', 'RandomStandardNormal', 'RandomUniform', 'RandomUniformInt', 'Range', 'RangeDataset', 'Rank', 'ReadFile', 'ReadVariableOp', 'ReaderNumRecordsProduced', 'ReaderNumRecordsProducedV2', 'ReaderNumWorkUnitsCompleted', 'ReaderNumWorkUnitsCompletedV2', 'ReaderRead', 'ReaderReadUpTo', 'ReaderReadUpToV2', 'ReaderReadV2', 'ReaderReset', 'ReaderResetV2', 'ReaderRestoreState', 'ReaderRestoreStateV2', 'ReaderSerializeState', 'ReaderSerializeStateV2', 'Real', 'RealDiv', 'RebatchDataset', 'Reciprocal', 'ReciprocalGrad', 'RecordInput', 'Recv', 'RecvTPUEmbeddingActivations', 'ReduceDataset', 'ReduceJoin', 'RefEnter', 'RefExit', 'RefIdentity', 'RefMerge', 'RefNextIteration', 'RefSelect', 'RefSwitch', 'RegexFullMatch', 'RegexReplace', 'Relu', 'Relu6', 'Relu6Grad', 'ReluGrad', 'RemoteCall', 'RepeatDataset', 'RequantizationRange', 'RequantizationRangePerChannel', 'Requantize', 'RequantizePerChannel', 'Reshape', 'ResizeArea', 'ResizeBicubic', 'ResizeBicubicGrad', 'ResizeBilinear', 'ResizeBilinearGrad', 'ResizeNearestNeighbor', 'ResizeNearestNeighborGrad', 'ResourceAccumulatorApplyGradient', 'ResourceAccumulatorNumAccumulated', 'ResourceAccumulatorSetGlobalStep', 'ResourceAccumulatorTakeGradient', 'ResourceApplyAdaMax', 'ResourceApplyAdadelta', 'ResourceApplyAdagrad', 'ResourceApplyAdagradDA', 'ResourceApplyAdagradV2', 'ResourceApplyAdam', 'ResourceApplyAdamWithAmsgrad', 'ResourceApplyAddSign', 'ResourceApplyCenteredRMSProp', 'ResourceApplyFtrl', 'ResourceApplyFtrlV2', 'ResourceApplyGradientDescent', 'ResourceApplyKerasMomentum', 'ResourceApplyMomentum', 'ResourceApplyPowerSign', 'ResourceApplyProximalAdagrad', 'ResourceApplyProximalGradientDescent', 'ResourceApplyRMSProp', 'ResourceConditionalAccumulator', 'ResourceCountUpTo', 'ResourceGather', 'ResourceGatherNd', 'ResourceScatterAdd', 'ResourceScatterDiv', 'ResourceScatterMax', 'ResourceScatterMin', 'ResourceScatterMul', 'ResourceScatterNdAdd', 'ResourceScatterNdSub', 'ResourceScatterNdUpdate', 'ResourceScatterSub', 'ResourceScatterUpdate', 'ResourceSparseApplyAdadelta', 'ResourceSparseApplyAdagrad', 'ResourceSparseApplyAdagradDA', 'ResourceSparseApplyAdagradV2', 'ResourceSparseApplyCenteredRMSProp', 'ResourceSparseApplyFtrl', 'ResourceSparseApplyFtrlV2', 'ResourceSparseApplyKerasMomentum', 'ResourceSparseApplyMomentum', 'ResourceSparseApplyProximalAdagrad', 'ResourceSparseApplyProximalGradientDescent', 'ResourceSparseApplyRMSProp', 'ResourceStridedSliceAssign', 'Restore', 'RestoreSlice', 'RestoreV2', 'RetrieveTPUEmbeddingADAMParameters', 'RetrieveTPUEmbeddingADAMParametersGradAccumDebug', 'RetrieveTPUEmbeddingAdadeltaParameters', 'RetrieveTPUEmbeddingAdadeltaParametersGradAccumDebug', 'RetrieveTPUEmbeddingAdagradParameters', 'RetrieveTPUEmbeddingAdagradParametersGradAccumDebug', 'RetrieveTPUEmbeddingCenteredRMSPropParameters', 'RetrieveTPUEmbeddingFTRLParameters', 'RetrieveTPUEmbeddingFTRLParametersGradAccumDebug', 'RetrieveTPUEmbeddingMDLAdagradLightParameters', 'RetrieveTPUEmbeddingMomentumParameters', 'RetrieveTPUEmbeddingMomentumParametersGradAccumDebug', 'RetrieveTPUEmbeddingProximalAdagradParameters', 'RetrieveTPUEmbeddingProximalAdagradParametersGradAccumDebug', 'RetrieveTPUEmbeddingRMSPropParameters', 'RetrieveTPUEmbeddingRMSPropParametersGradAccumDebug', 'RetrieveTPUEmbeddingStochasticGradientDescentParameters', 'Reverse', 'ReverseSequence', 'ReverseV2', 'RightShift', 'Rint', 'RngSkip', 'Roll', 'Round', 'Rsqrt', 'RsqrtGrad', 'SampleDistortedBoundingBox', 'SampleDistortedBoundingBoxV2', 'SamplingDataset', 'Save', 'SaveSlices', 'SaveV2', 'ScalarSummary', 'ScaleAndTranslate', 'ScaleAndTranslateGrad', 'ScanDataset', 'ScatterAdd', 'ScatterDiv', 'ScatterMax', 'ScatterMin', 'ScatterMul', 'ScatterNd', 'ScatterNdAdd', 'ScatterNdNonAliasingAdd', 'ScatterNdSub', 'ScatterNdUpdate', 'ScatterSub', 'ScatterUpdate', 'SdcaFprint', 'SdcaOptimizer', 'SdcaOptimizerV2', 'SdcaShrinkL1', 'SegmentMax', 'SegmentMean', 'SegmentMin', 'SegmentProd', 'SegmentSum', 'Select', 'SelectV2', 'SelfAdjointEig', 'SelfAdjointEigV2', 'Selu', 'SeluGrad', 'Send', 'SendTPUEmbeddingGradients', 'SerializeIterator', 'SerializeManySparse', 'SerializeSparse', 'SerializeTensor', 'SetSize', 'SetStatsAggregatorDataset', 'Shape', 'ShapeN', 'ShardDataset', 'ShardedFilename', 'ShardedFilespec', 'ShuffleAndRepeatDataset', 'ShuffleDataset', 'ShuffleDatasetV2', 'ShutdownDistributedTPU', 'Sigmoid', 'SigmoidGrad', 'Sign', 'Sin', 'Sinh', 'Size', 'SkipDataset', 'SleepDataset', 'Slice', 'SlidingWindowDataset', 'Snapshot', 'SnapshotDataset', 'SobolSample', 'Softmax', 'SoftmaxCrossEntropyWithLogits', 'Softplus', 'SoftplusGrad', 'Softsign', 'SoftsignGrad', 'SpaceToBatch', 'SpaceToBatchND', 'SpaceToDepth', 'SparseAccumulatorApplyGradient', 'SparseAccumulatorTakeGradient', 'SparseAdd', 'SparseAddGrad', 'SparseApplyAdadelta', 'SparseApplyAdagrad', 'SparseApplyAdagradDA', 'SparseApplyAdagradV2', 'SparseApplyCenteredRMSProp', 'SparseApplyFtrl', 'SparseApplyFtrlV2', 'SparseApplyMomentum', 'SparseApplyProximalAdagrad', 'SparseApplyProximalGradientDescent', 'SparseApplyRMSProp', 'SparseConcat', 'SparseConditionalAccumulator', 'SparseCross', 'SparseDenseCwiseAdd', 'SparseDenseCwiseDiv', 'SparseDenseCwiseMul', 'SparseFillEmptyRows', 'SparseFillEmptyRowsGrad', 'SparseMatMul', 'SparseMatrixAdd', 'SparseMatrixMatMul', 'SparseMatrixMul', 'SparseMatrixNNZ', 'SparseMatrixOrderingAMD', 'SparseMatrixSoftmax', 'SparseMatrixSoftmaxGrad', 'SparseMatrixSparseCholesky', 'SparseMatrixSparseMatMul', 'SparseMatrixTranspose', 'SparseMatrixZeros', 'SparseReduceMax', 'SparseReduceMaxSparse', 'SparseReduceSum', 'SparseReduceSumSparse', 'SparseReorder', 'SparseReshape', 'SparseSegmentMean', 'SparseSegmentMeanGrad', 'SparseSegmentMeanWithNumSegments', 'SparseSegmentSqrtN', 'SparseSegmentSqrtNGrad', 'SparseSegmentSqrtNWithNumSegments', 'SparseSegmentSum', 'SparseSegmentSumWithNumSegments', 'SparseSlice', 'SparseSliceGrad', 'SparseSoftmax', 'SparseSoftmaxCrossEntropyWithLogits', 'SparseSparseMaximum', 'SparseSparseMinimum', 'SparseSplit', 'SparseTensorDenseAdd', 'SparseTensorDenseMatMul', 'SparseTensorSliceDataset', 'SparseTensorToCSRSparseMatrix', 'SparseToDense', 'SparseToSparseSetOperation', 'Spence', 'Split', 'SplitV', 'SqlDataset', 'Sqrt', 'SqrtGrad', 'Square', 'SquaredDifference', 'Squeeze', 'Stack', 'StackClose', 'StackCloseV2', 'StackPop', 'StackPopV2', 'StackPush', 'StackPushV2', 'StackV2', 'Stage', 'StageClear', 'StagePeek', 'StageSize', 'StatefulPartitionedCall', 'StatefulRandomBinomial', 'StatefulStandardNormal', 'StatefulStandardNormalV2', 'StatefulTruncatedNormal', 'StatefulUniform', 'StatefulUniformFullInt', 'StatefulUniformInt', 'StatelessIf', 'StatelessMultinomial', 'StatelessRandomBinomial', 'StatelessRandomGammaV2', 'StatelessRandomNormal', 'StatelessRandomPoisson', 'StatelessRandomUniform', 'StatelessRandomUniformFullInt', 'StatelessRandomUniformInt', 'StatelessTruncatedNormal', 'StatelessWhile', 'StaticRegexFullMatch', 'StaticRegexReplace', 'StatsAggregatorHandle', 'StatsAggregatorHandleV2', 'StatsAggregatorSetSummaryWriter', 'StatsAggregatorSummary', 'StopGradient', 'StridedSlice', 'StridedSliceAssign', 'StridedSliceGrad', 'StringFormat', 'StringJoin', 'StringLength', 'StringLower', 'StringNGrams', 'StringSplit', 'StringSplitV2', 'StringStrip', 'StringToHashBucket', 'StringToHashBucketFast', 'StringToHashBucketStrong', 'StringToNumber', 'StringUpper', 'Sub', 'Substr', 'Sum', 'SummaryWriter', 'Svd', 'Switch', 'SymbolicGradient', 'TFRecordDataset', 'TFRecordReader', 'TFRecordReaderV2', 'TPUCompilationResult', 'TPUEmbeddingActivations', 'TPUOrdinalSelector', 'TPUPartitionedCall', 'TPUReplicateMetadata', 'TPUReplicatedInput', 'TPUReplicatedOutput', 'TakeDataset', 'TakeManySparseFromTensorsMap', 'TakeWhileDataset', 'Tan', 'Tanh', 'TanhGrad', 'TemporaryVariable', 'TensorArray', 'TensorArrayClose', 'TensorArrayCloseV2', 'TensorArrayCloseV3', 'TensorArrayConcat', 'TensorArrayConcatV2', 'TensorArrayConcatV3', 'TensorArrayGather', 'TensorArrayGatherV2', 'TensorArrayGatherV3', 'TensorArrayGrad', 'TensorArrayGradV2', 'TensorArrayGradV3', 'TensorArrayGradWithShape', 'TensorArrayPack', 'TensorArrayRead', 'TensorArrayReadV2', 'TensorArrayReadV3', 'TensorArrayScatter', 'TensorArrayScatterV2', 'TensorArrayScatterV3', 'TensorArraySize', 'TensorArraySizeV2', 'TensorArraySizeV3', 'TensorArraySplit', 'TensorArraySplitV2', 'TensorArraySplitV3', 'TensorArrayUnpack', 'TensorArrayV2', 'TensorArrayV3', 'TensorArrayWrite', 'TensorArrayWriteV2', 'TensorArrayWriteV3', 'TensorDataset', 'TensorListConcat', 'TensorListConcatLists', 'TensorListConcatV2', 'TensorListElementShape', 'TensorListFromTensor', 'TensorListGather', 'TensorListGetItem', 'TensorListLength', 'TensorListPopBack', 'TensorListPushBack', 'TensorListPushBackBatch', 'TensorListReserve', 'TensorListResize', 'TensorListScatter', 'TensorListScatterIntoExistingList', 'TensorListScatterV2', 'TensorListSetItem', 'TensorListSplit', 'TensorListStack', 'TensorScatterAdd', 'TensorScatterSub', 'TensorScatterUpdate', 'TensorSliceDataset', 'TensorStridedSliceUpdate', 'TensorSummary', 'TensorSummaryV2', 'TextLineDataset', 'TextLineReader', 'TextLineReaderV2', 'ThreadPoolDataset', 'ThreadPoolHandle', 'ThreadUnsafeUnigramCandidateSampler', 'Tile', 'TileGrad', 'Timestamp', 'ToBool', 'TopK', 'TopKV2', 'Transpose', 'TridiagonalMatMul', 'TridiagonalSolve', 'TruncateDiv', 'TruncateMod', 'TruncatedNormal', 'Unbatch', 'UnbatchDataset', 'UnbatchGrad', 'UnicodeDecode', 'UnicodeDecodeWithOffsets', 'UnicodeEncode', 'UnicodeScript', 'UnicodeTranscode', 'UniformCandidateSampler', 'Unique', 'UniqueDataset', 'UniqueV2', 'UniqueWithCounts', 'UniqueWithCountsV2', 'Unpack', 'UnravelIndex', 'UnsortedSegmentJoin', 'UnsortedSegmentMax', 'UnsortedSegmentMin', 'UnsortedSegmentProd', 'UnsortedSegmentSum', 'Unstage', 'UnwrapDatasetVariant', 'UpperBound', 'VarHandleOp', 'VarIsInitializedOp', 'Variable', 'VariableShape', 'VariableV2', 'Where', 'While', 'WholeFileReader', 'WholeFileReaderV2', 'WindowDataset', 'WorkerHeartbeat', 'WrapDatasetVariant', 'WriteAudioSummary', 'WriteFile', 'WriteGraphSummary', 'WriteHistogramSummary', 'WriteImageSummary', 'WriteRawProtoSummary', 'WriteScalarSummary', 'WriteSummary', 'Xdivy', 'Xlog1py', 'Xlogy', 'ZerosLike', 'Zeta', 'ZipDataset', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '_sys'])

print ( 'MatMul' in operations )