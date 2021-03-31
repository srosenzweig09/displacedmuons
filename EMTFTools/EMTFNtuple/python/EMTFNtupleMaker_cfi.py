import FWCore.ParameterSet.Config as cms

EMTFNtuple = cms.EDAnalyzer('EMTFNtuple',

    CSCInputTag      = cms.InputTag('simCscTriggerPrimitiveDigis','MPCSORTED'), 
    RPCInputTag      = cms.InputTag('simMuonRPCDigis'), 
    CPPFInputTag     = cms.InputTag('simCPPFDigis'), 
    GEMInputTag      = cms.InputTag('simMuonGEMPadDigiClusters'), 

    IRPCInputTag     = cms.InputTag('simMuonRPCDigis'), 
    ME0InputTag      = cms.InputTag('me0TriggerConvertedPseudoDigis'), 
    DTInputTag       = cms.InputTag('simDtTriggerPrimitiveDigis'), 

    EMTFHitTag       = cms.InputTag('simEmtfDigis'),
    EMTFUnpHitTag    = cms.InputTag('emtfDigis', 'EMTF'),
    
    EMTFTrackTag     = cms.InputTag('simEmtfDigis'),
    EMTFUnpTrackTag  = cms.InputTag('gmtStage2Digis', 'EMTF'),

    GMTMuonTag       = cms.InputTag('simGmtStage2Digis'),
    GMTUnpMuonTag    = cms.InputTag('gmtStage2Digis', 'Muon'),

    GENPartTag       = cms.InputTag('genParticles'),

    outFileName      = cms.string('EMTFNtuple.root'),
    verbosity        = cms.untracked.int32(0),

    # Change defaults to enable/disable processing of various inputs
    enablePhase2     = cms.bool(False),

    useCSC           = cms.bool(True),
    useRPC           = cms.bool(False),
    useCPPF          = cms.bool(False),
    useGEM           = cms.bool(False),

    useIRPC          = cms.bool(False),
    useME0           = cms.bool(False),
    useDT            = cms.bool(False),


    useEMTFHits      = cms.bool(False),
    useEMTFUnpHits   = cms.bool(False),
    
    useEMTFTracks    = cms.bool(False),
    useEMTFUnpTracks = cms.bool(False),
    
    useGMTMuons      = cms.bool(False),
    useGMTUnpMuons   = cms.bool(False),
    
    useGENParts      = cms.bool(False),
    useEventInfo     = cms.bool(False),

  )