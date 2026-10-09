# CoreIPC changes from ios-26.5.2 to ios-27.0.1

| | ios-26.5.2 | ios-27.0.1 |
| --- | --- | --- |
| Platform | iOS | iOS |
| WebKit | 624.2.5.10.8 | 625.1.29.10.33 |
| Messages | 3620 | 3710 |
| Receivers | 220 | 218 |

- 405 messages added and 315 removed
- 6 messages changed route or flags
- 3260 messages kept their names but changed numbers
- New receivers: `ProxyingNetworkAgent`, `ProxyingPageAgent`, `RemoteMediaResourceLoader`, `RemoteMediaResourceLoaderProxy`, `RemoteMesh`
- Removed receivers: `IPCTesterReceiverSwift`, `MediaSourcePrivateRemoteMessageReceiver`, `RemoteDDMesh`, `RemoteMediaResourceManager`, `RemoteMediaSourceProxy`, `RemoteSourceBufferProxy`, `SourceBufferPrivateRemoteMessageReceiver`

## Changes per receiver

| Receiver | Added | Removed |
| --- | --- | --- |
| LogStream | 234 | 186 |
| WebPageProxy | 24 | 26 |
| WebPage | 30 | 9 |
| RemoteSourceBufferProxy | 0 | 34 |
| RemoteMesh | 14 | 0 |
| NetworkProcess | 10 | 0 |
| RemoteDDMesh | 0 | 9 |
| RemoteGraphicsContextGL | 2 | 6 |
| RemoteMediaSourceProxy | 0 | 8 |
| SourceBufferPrivateRemoteMessageReceiver | 0 | 8 |
| MediaPlayerPrivateRemote | 2 | 5 |
| RemoteMediaResourceLoader | 7 | 0 |
| RemoteMediaResourceManager | 0 | 7 |
| ProxyingNetworkAgent | 6 | 0 |
| RemoteAudioVideoRendererProxyManager | 5 | 1 |
| WebInspectorBackend | 6 | 0 |
| GPUConnectionToWebProcess | 3 | 2 |
| RemoteAudioSourceProviderManager | 4 | 1 |
| WebProcess | 4 | 1 |
| NetworkProcessProxy | 3 | 1 |
| ProxyingPageAgent | 4 | 0 |
| RemoteGraphicsContext | 3 | 1 |
| RemoteMediaPlayerProxy | 2 | 2 |
| GPUProcess | 2 | 1 |
| NetworkConnectionToWebProcess | 2 | 1 |
| NetworkStorageManager | 3 | 0 |
| RemoteMediaResourceLoaderProxy | 3 | 0 |
| WebFrame | 3 | 0 |
| WebPageTesting | 3 | 0 |
| AudioVideoRendererRemoteMessageReceiver | 1 | 1 |
| RemoteRenderingBackend | 2 | 0 |
| WebAutomationSession | 2 | 0 |
| WebAutomationSessionProxy | 2 | 0 |
| WebBackForwardList | 1 | 1 |
| WebExtensionContext | 2 | 0 |
| WebFrameProxy | 2 | 0 |
| WebProcessProxy | 1 | 1 |
| WebResourceLoader | 1 | 1 |
| IPCTesterReceiverSwift | 0 | 1 |
| LibWebRTCCodecsProxy | 1 | 0 |
| MediaSourcePrivateRemoteMessageReceiver | 0 | 1 |
| ModelProcessModelPlayer | 1 | 0 |
| NetworkProcessConnection | 1 | 0 |
| PlatformXRSystemProxy | 1 | 0 |
| PushClientConnection | 1 | 0 |
| RemoteBuffer | 1 | 0 |
| RemoteGPU | 1 | 0 |
| RemoteImageBufferSet | 1 | 0 |
| RemoteLayerTreeDrawingAreaProxy | 1 | 0 |
| SampleBufferDisplayLayer | 1 | 0 |
| WasmDebuggerDispatcher | 1 | 0 |
| WebInspectorUI | 1 | 0 |

## Added (405)

| Message | Number | Route | Flags |
| --- | --- | --- | --- |
| `AudioVideoRendererRemoteMessageReceiver_UpdatePlaybackQualityMetrics` | 15 | GPU -> WebContent |  |
| `GPUConnectionToWebProcess_CanDecodeExtendedType` | 60 | WebContent -> GPU | async reply |
| `GPUConnectionToWebProcess_SetDisplayCaptureEnvironment` | 77 | WebContent -> GPU |  |
| `GPUConnectionToWebProcess_SetMediaPlaybackEnvironment` | 79 | WebContent -> GPU |  |
| `GPUProcess_CancelGetDisplayMediaPrompt` | 97 | UI -> GPU |  |
| `GPUProcess_PromptForGetDisplayMedia` | 109 | UI -> GPU | async reply |
| `LibWebRTCCodecsProxy_SetDecoderColorSpaceOverride` | 187 | WebContent -> GPU |  |
| `LogStream_CachedRawResourceRedirectReceived` | 206 | WebContent -> UI | stream |
| `LogStream_CachedResourceLoadNoAssociatedFrame` | 207 | WebContent -> UI | stream |
| `LogStream_CachedResourceRedirectReceived` | 208 | WebContent -> UI | stream |
| `LogStream_CoreIpcNsurlRequestPropertyKeyNotAllowed` | 209 | WebContent -> UI | stream |
| `LogStream_DocumentLoaderAttachToFrame` | 210 | WebContent -> UI | stream |
| `LogStream_DocumentLoaderCancelMainResourceLoad` | 211 | WebContent -> UI | stream |
| `LogStream_DocumentLoaderDetachFromFrame` | 212 | WebContent -> UI | stream |
| `LogStream_DocumentLoaderMainReceivedError` | 213 | WebContent -> UI | stream |
| `LogStream_DocumentLoaderNotifyFinishedCancelingLoad` | 214 | WebContent -> UI | stream |
| `LogStream_DocumentLoaderSetMainDocumentError` | 215 | WebContent -> UI | stream |
| `LogStream_DocumentLoaderStartLoadingMainResourceEmptyDocument` | 216 | WebContent -> UI | stream |
| `LogStream_DocumentLoaderStartLoadingMainResourceStartingLoad` | 217 | WebContent -> UI | stream |
| `LogStream_DocumentLoaderStopLoading` | 218 | WebContent -> UI | stream |
| `LogStream_FontCacheCoreTextRegisterError` | 219 | WebContent -> UI | stream |
| `LogStream_FontCacheCoreTextRegisterFont` | 220 | WebContent -> UI | stream |
| `LogStream_FrameLoaderChangeLocation` | 221 | WebContent -> UI | stream |
| `LogStream_FrameLoaderCheckLoadCompleteForThisFrame` | 222 | WebContent -> UI | stream |
| `LogStream_FrameLoaderCheckLoadCompleteForThisFrameFailedProvisionalLoad` | 223 | WebContent -> UI | stream |
| `LogStream_FrameLoaderClearProvisionalLoad` | 224 | WebContent -> UI | stream |
| `LogStream_FrameLoaderContinueLoadAfterNavigationPolicy` | 225 | WebContent -> UI | stream |
| `LogStream_FrameLoaderContinueLoadAfterNavigationPolicyCannotContinue` | 226 | WebContent -> UI | stream |
| `LogStream_FrameLoaderLoadDocumentLoader` | 227 | WebContent -> UI | stream |
| `LogStream_FrameLoaderLoadFrameLoadRequest` | 228 | WebContent -> UI | stream |
| `LogStream_FrameLoaderLoadFrameRequestFrameLoadStarted` | 229 | WebContent -> UI | stream |
| `LogStream_FrameLoaderLoadUrl` | 230 | WebContent -> UI | stream |
| `LogStream_FrameLoaderLoadUrlIntoChildFrame` | 231 | WebContent -> UI | stream |
| `LogStream_FrameLoaderLoadWithDocumentLoaderFrameLoadStarted` | 232 | WebContent -> UI | stream |
| `LogStream_FrameLoaderLoadWithDocumentLoaderMainFrameLoadStarted` | 233 | WebContent -> UI | stream |
| `LogStream_FrameLoaderLoadWithNavigationAction` | 234 | WebContent -> UI | stream |
| `LogStream_FrameLoaderPrepareForLoadStart` | 235 | WebContent -> UI | stream |
| `LogStream_FrameLoaderReload` | 236 | WebContent -> UI | stream |
| `LogStream_FrameLoaderSetDocumentLoader` | 237 | WebContent -> UI | stream |
| `LogStream_FrameLoaderSetPolicyDocumentLoader` | 238 | WebContent -> UI | stream |
| `LogStream_FrameLoaderSetProvisionalDocumentLoader` | 239 | WebContent -> UI | stream |
| `LogStream_FrameLoaderSetStateMainFrameLoadCompleted` | 240 | WebContent -> UI | stream |
| `LogStream_FrameLoaderStopAllLoaders` | 241 | WebContent -> UI | stream |
| `LogStream_FrameLoaderStopAllLoadersClearingProvisionalDocumentLoader` | 242 | WebContent -> UI | stream |
| `LogStream_FrameLoaderTransitionToCommitted` | 243 | WebContent -> UI | stream |
| `LogStream_GpuProcessConnectionCreate` | 244 | WebContent -> UI | stream |
| `LogStream_GpuProcessConnectionDidInitialize` | 245 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementAddAudioTrack` | 246 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementAddVideoTrack` | 247 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementApplyConfiguration` | 248 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementCanPlayType` | 249 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementCanTransitionFromAutoplayToPlayNotAutoplaying` | 250 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementCanTransitionFromAutoplayToPlayNotEnoughData` | 251 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementCancelSpeakingCueText` | 252 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementCheckPlaybackTargetCompatibility` | 253 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementConfigureTextTrackDisplay` | 254 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementConfigureTextTrackGroup` | 255 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementConstructor` | 256 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementCreateMediaPlayer` | 257 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementCurrentMediaTimeSeeking` | 258 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementDestructor` | 259 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementDidMoveToNewDocument` | 260 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementDispatchPlayPauseEventsIfNeedsQuirks` | 261 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementExitFullscreen` | 262 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementFinishSeek` | 263 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementHardwareMutedStateDidChange` | 264 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementInsertionSteps` | 265 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementLoadNextSourceChild` | 266 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementMediaEngineWasUpdated` | 267 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementMediaPlayerCharacteristicsChanged` | 268 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementMediaPlayerCharacteristicsChangedNoMediaSession` | 269 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementMediaPlayerDurationChanged` | 270 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementMediaPlayerEngineUpdated` | 271 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementMediaPlayerMuteChanged` | 272 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementMediaPlayerRateChanged` | 273 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementMediaPlayerResourceNotSupported` | 274 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementMediaPlayerSizeChanged` | 275 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementMediaPlayerTimeChanged` | 276 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementMediaPlayerTimeChangedLooping` | 277 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementMediaPlayerVolumeChanged` | 278 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementMediaStreamCaptureStarted` | 279 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementNoneSupported` | 280 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementPause` | 281 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementPauseInternal` | 282 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementPausePlaybackForExtendedTextDescription` | 283 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementPauseSpeakingCueText` | 284 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementPlay` | 285 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementPlayDom` | 286 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementPlayInternal` | 287 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementPostConnectionSteps` | 288 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementPrepareForLoad` | 289 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementPurgeBufferedDataIfPossible` | 290 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementRebuildMediaEngineForWirelessPlayback` | 291 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementRemoveAudioTrack` | 292 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementRemovingSteps` | 293 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementResume` | 294 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementResumeSpeakingCueText` | 295 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementSceneIdentifierDidChange` | 296 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementScheduleConfigureTextTracksLambdaTaskFired` | 297 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementScheduleConfigureTextTracksTaskScheduled` | 298 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementScheduleMediaEngineWasUpdatedLambdaTaskFired` | 299 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementScheduleMediaEngineWasUpdatedTaskScheduled` | 300 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementSeekInternal` | 301 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementSeekWithTolerance` | 302 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementSelectMediaResourceAttemptingUseOfUnattachedMediaSourceHandle` | 303 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementSelectMediaResourceEmptySrc` | 304 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementSelectMediaResourceHasSrcAttrPlayerNotCreated` | 305 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementSelectMediaResourceLambdaTaskFired` | 306 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementSelectMediaResourceNothingToLoad` | 307 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementSelectMediaResourceUsingSrcAttributeUrl` | 308 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementSelectMediaResourceUsingSrcObjectProperty` | 309 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementSetAutoplayEventPlaybackState` | 310 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementSetBufferingPolicy` | 311 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementSetMutedInternal` | 312 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementSetNetworkState` | 313 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementSetPlaybackRate` | 314 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementSetPlayerIdentifierForVideoElement` | 315 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementSetReadyState` | 316 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementSetShouldDelayLoadEvent` | 317 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementSetShowPosterFlag` | 318 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementSetVolume` | 319 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementStop` | 320 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementUpdatePlayState` | 321 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementUpdateShouldPlay` | 322 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementUserDidInterfereWithAutoplay` | 323 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementVisibilityStateChanged` | 324 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementWaitForSourceChange` | 325 | WebContent -> UI | stream |
| `LogStream_HTMLMediaElementWebkitShowPlaybackTargetPicker` | 326 | WebContent -> UI | stream |
| `LogStream_HTMLVideoElementMediaPlayerFirstVideoFrameAvailable` | 327 | WebContent -> UI | stream |
| `LogStream_HTMLVideoElementMediaPlayerRenderingModeChanged` | 328 | WebContent -> UI | stream |
| `LogStream_HTMLVideoElementScheduleResizeEvent` | 329 | WebContent -> UI | stream |
| `LogStream_LibWebRtcLogError` | 330 | WebContent -> UI | stream |
| `LogStream_LibWebRtcLogMessage` | 331 | WebContent -> UI | stream |
| `LogStream_LibWebRtcMediaEndpointOnStatsDelivered` | 332 | WebContent -> UI | stream |
| `LogStream_LocalFrameViewFiringFirstVisuallyNonEmptyLayoutMilestone` | 333 | WebContent -> UI | stream |
| `LogStream_LocalFrameViewFiringResizeEventsDisabledForPage` | 334 | WebContent -> UI | stream |
| `LogStream_LocalFrameViewNotPaintingLayoutNeeded` | 335 | WebContent -> UI | stream |
| `LogStream_MediaPlayerPrivateRemoteLayerHostingContextChanged` | 337 | WebContent -> UI | stream |
| `LogStream_MediaSessionManagerCocoaClientCharacteristicsChanged` | 338 | WebContent -> UI | stream |
| `LogStream_MediaSessionManagerCocoaSessionCanProduceAudioChanged` | 339 | WebContent -> UI | stream |
| `LogStream_MediaSessionManagerCocoaUpdateSessionState` | 340 | WebContent -> UI | stream |
| `LogStream_MediaSessionManagerInterfaceAddSession` | 341 | WebContent -> UI | stream |
| `LogStream_MediaSessionManagerInterfaceMaybeActivateAudioSessionActiveSessionNotRequired` | 342 | WebContent -> UI | stream |
| `LogStream_MediaSessionManagerInterfaceRemoveSession` | 343 | WebContent -> UI | stream |
| `LogStream_MediaSessionManagerInterfaceSessionCanProduceAudioChanged` | 344 | WebContent -> UI | stream |
| `LogStream_MediaSessionManagerInterfaceSessionWillEndPlayback` | 345 | WebContent -> UI | stream |
| `LogStream_PeerConnectionBackendCreateAnswerSucceeded` | 346 | WebContent -> UI | stream |
| `LogStream_PeerConnectionBackendCreateOfferSucceeded` | 347 | WebContent -> UI | stream |
| `LogStream_PerformanceLoggingMemoryUsageForKey` | 348 | WebContent -> UI | stream |
| `LogStream_PerformanceLoggingMemoryUsageInfo` | 349 | WebContent -> UI | stream |
| `LogStream_PerformanceMonitorMeasureCpuUsageInActivityState` | 350 | WebContent -> UI | stream |
| `LogStream_PerformanceMonitorMeasurePostBackgroundCpuUsage` | 351 | WebContent -> UI | stream |
| `LogStream_PerformanceMonitorMeasurePostBackgroundMemoryUsage` | 352 | WebContent -> UI | stream |
| `LogStream_PerformanceMonitorMeasurePostLoadCpuUsage` | 353 | WebContent -> UI | stream |
| `LogStream_PerformanceMonitorMeasurePostLoadMemoryUsage` | 354 | WebContent -> UI | stream |
| `LogStream_PlatformInitializeWebProcess` | 355 | WebContent -> UI | stream |
| `LogStream_PolicyCheckerCheckNavigationPolicyContinueInitialEmptyDocument` | 356 | WebContent -> UI | stream |
| `LogStream_PolicyCheckerCheckNavigationPolicyContinueLoadInAnotherProcess` | 357 | WebContent -> UI | stream |
| `LogStream_PolicyCheckerCheckNavigationPolicyContinuePolicyActionIsUse` | 358 | WebContent -> UI | stream |
| `LogStream_ProgressTrackerFinalProgressComplete` | 359 | WebContent -> UI | stream |
| `LogStream_ProgressTrackerProgressCompleted` | 360 | WebContent -> UI | stream |
| `LogStream_ProgressTrackerProgressStarted` | 361 | WebContent -> UI | stream |
| `LogStream_ReceivedLaunchServicesDatabase` | 362 | WebContent -> UI | stream |
| `LogStream_RemoteRenderingBackendProxyCreatedRenderingBackend` | 363 | WebContent -> UI | stream |
| `LogStream_ResourceLoaderWillSendRequestInternal` | 364 | WebContent -> UI | stream |
| `LogStream_ResourceLoaderWillSendRequestInternalCrossOriginRedirect` | 365 | WebContent -> UI | stream |
| `LogStream_RtcPeerConnectionSetLocalDescription` | 366 | WebContent -> UI | stream |
| `LogStream_RtcPeerConnectionSetRemoteDescription` | 367 | WebContent -> UI | stream |
| `LogStream_ServiceWorkerThreadProxyRemoveFetch` | 368 | WebContent -> UI | stream |
| `LogStream_SubResourceLoaderDidFail` | 369 | WebContent -> UI | stream |
| `LogStream_SubResourceLoaderDidFinishLoading` | 370 | WebContent -> UI | stream |
| `LogStream_SubResourceLoaderDidFinishLoadingCanceled` | 371 | WebContent -> UI | stream |
| `LogStream_SubResourceLoaderDidFinishLoadingDidNotReachTerminalState` | 372 | WebContent -> UI | stream |
| `LogStream_SubResourceLoaderDidFinishLoadingReachedTerminalState` | 373 | WebContent -> UI | stream |
| `LogStream_SubResourceLoaderDidReceiveResponseCancelingLoadBecauseOfCrossOriginAccessControl` | 374 | WebContent -> UI | stream |
| `LogStream_SubResourceLoaderDidReceiveResponseCancelingLoadBecauseOfMultipartNonImage` | 375 | WebContent -> UI | stream |
| `LogStream_SubResourceLoaderDidReceiveResponseCancelingLoadBlockedByContentPolicy` | 376 | WebContent -> UI | stream |
| `LogStream_SubResourceLoaderDidReceiveResponseCancelingLoadReceivedUnexpectedRangeResponse` | 377 | WebContent -> UI | stream |
| `LogStream_SubResourceLoaderWillCancel` | 378 | WebContent -> UI | stream |
| `LogStream_SubResourceLoaderWillSendRequestInternal` | 379 | WebContent -> UI | stream |
| `LogStream_SubResourceLoaderWillSendRequestInternalCancelledInvalidNewRequest` | 380 | WebContent -> UI | stream |
| `LogStream_SubResourceLoaderWillSendRequestInternalCancelledInvalidRequest` | 381 | WebContent -> UI | stream |
| `LogStream_SubResourceLoaderWillSendRequestInternalCancelledTerminalState` | 382 | WebContent -> UI | stream |
| `LogStream_SubResourceLoaderWillSendRequestInternalReachedTerminalState` | 383 | WebContent -> UI | stream |
| `LogStream_SubResourceLoaderWillSendRequestInternalResourceDoneNotifyingClients` | 384 | WebContent -> UI | stream |
| `LogStream_SubResourceLoaderWillSendRequestInternalResourceLoadCancelledAfterImageBeingDeferred` | 385 | WebContent -> UI | stream |
| `LogStream_SubResourceLoaderWillSendRequestInternalResourceLoadCancelledAfterRedirectDeniedByCorsPolicy` | 386 | WebContent -> UI | stream |
| `LogStream_SubResourceLoaderWillSendRequestInternalResourceLoadCancelledAfterUsingBlockedPort` | 387 | WebContent -> UI | stream |
| `LogStream_SubResourceLoaderWillSendRequestInternalResourceLoadCancelledCannotRequestAfterRedirection` | 388 | WebContent -> UI | stream |
| `LogStream_SubResourceLoaderWillSendRequestInternalResourceLoadCancelledDataURL` | 389 | WebContent -> UI | stream |
| `LogStream_SubResourceLoaderWillSendRequestInternalResourceLoadCancelledRedirectNotAllowed` | 390 | WebContent -> UI | stream |
| `LogStream_SubResourceLoaderWillSendRequestInternalResourceLoadCancelledTooManyRedirects` | 391 | WebContent -> UI | stream |
| `LogStream_SubResourceLoaderWillSendRequestInternalResourceLoadCompleted` | 392 | WebContent -> UI | stream |
| `LogStream_SubResourceLoaderWillSendRequestInternalResourceLoadFinished` | 393 | WebContent -> UI | stream |
| `LogStream_SubResourceLoaderWillSendRequestInternalTerminalStateCallingCompletionHandler` | 394 | WebContent -> UI | stream |
| `LogStream_TimedOutWaitingForLaunchServicesDatabaseUpdate` | 395 | WebContent -> UI | stream |
| `LogStream_UserActivityImplBeginActivity` | 396 | WebContent -> UI | stream |
| `LogStream_UserActivityImplEndActivity` | 397 | WebContent -> UI | stream |
| `LogStream_VideoPresentationManagerSetVideoLayerFrameFenced` | 398 | WebContent -> UI | stream |
| `LogStream_WaitingForLaunchServicesDatabaseUpdateTookFSeconds` | 399 | WebContent -> UI | stream |
| `LogStream_WebCoreTestLog` | 400 | WebContent -> UI | stream |
| `LogStream_WebFrameLoaderClientDispatchDecidePolicyForNavigationActionGotPolicyActionFromAsyncIpc` | 401 | WebContent -> UI | stream |
| `LogStream_WebFrameLoaderClientDispatchDecidePolicyForNavigationActionGotPolicyActionFromSyncIpc` | 402 | WebContent -> UI | stream |
| `LogStream_WebFrameLoaderClientDispatchDecidePolicyForNavigationActionSyncIpcFailed` | 403 | WebContent -> UI | stream |
| `LogStream_WebFrameLoaderClientNavigationActionDataEmptyRequest` | 404 | WebContent -> UI | stream |
| `LogStream_WebFrameLoaderClientNavigationActionDataNoFrame` | 405 | WebContent -> UI | stream |
| `LogStream_WebFrameLoaderClientNavigationActionDataNoWebPage` | 406 | WebContent -> UI | stream |
| `LogStream_WebLoaderStrategyScheduleLoad` | 407 | WebContent -> UI | stream |
| `LogStream_WebLoaderStrategyScheduleLoadResourceScheduledWithNetworkProcess` | 408 | WebContent -> UI | stream |
| `LogStream_WebLoaderStrategyScheduleLoadUrlLoadedAsData` | 409 | WebContent -> UI | stream |
| `LogStream_WebLocalFrameLoaderClientCompletePageTransitionIfNeeded` | 410 | WebContent -> UI | stream |
| `LogStream_WebLocalFrameLoaderClientDispatchDidFirstLayoutForFrame` | 411 | WebContent -> UI | stream |
| `LogStream_WebLocalFrameLoaderClientDispatchDidFirstVisuallyNonEmptyLayout` | 412 | WebContent -> UI | stream |
| `LogStream_WebLocalFrameLoaderClientDispatchDidReachLayoutMilestone` | 413 | WebContent -> UI | stream |
| `LogStream_WebPageClose` | 414 | WebContent -> UI | stream |
| `LogStream_WebPageDestructor` | 415 | WebContent -> UI | stream |
| `LogStream_WebPageFailedToMarkAllLayersVolatile` | 416 | WebContent -> UI | stream |
| `LogStream_WebPageFreezeLayerTree` | 417 | WebContent -> UI | stream |
| `LogStream_WebPageLoadRequest` | 418 | WebContent -> UI | stream |
| `LogStream_WebPageMarkLayersVolatile` | 419 | WebContent -> UI | stream |
| `LogStream_WebPageUnfreezeLayerTree` | 420 | WebContent -> UI | stream |
| `LogStream_WebProcessDestroyRenderingResources` | 421 | WebContent -> UI | stream |
| `LogStream_WebProcessFreezeAllLayerTrees` | 422 | WebContent -> UI | stream |
| `LogStream_WebProcessMarkAllLayersVolatile` | 423 | WebContent -> UI | stream |
| `LogStream_WebProcessPrepareToSuspend` | 424 | WebContent -> UI | stream |
| `LogStream_WebProcessReadyToSuspend` | 425 | WebContent -> UI | stream |
| `LogStream_WebResourceLoaderConstructor` | 426 | WebContent -> UI | stream |
| `LogStream_WebResourceLoaderDidBlockAuthenticationChallenge` | 427 | WebContent -> UI | stream |
| `LogStream_WebResourceLoaderDidFailResourceLoad` | 428 | WebContent -> UI | stream |
| `LogStream_WebResourceLoaderDidFinishResourceLoad` | 429 | WebContent -> UI | stream |
| `LogStream_WebResourceLoaderDidReceiveData` | 430 | WebContent -> UI | stream |
| `LogStream_WebResourceLoaderDidReceiveResource` | 431 | WebContent -> UI | stream |
| `LogStream_WebResourceLoaderDidReceiveResourceUnableToCreateFragmentedSharedBuffer` | 432 | WebContent -> UI | stream |
| `LogStream_WebResourceLoaderDidReceiveResponse` | 433 | WebContent -> UI | stream |
| `LogStream_WebResourceLoaderDidReceiveResponseNotContinuingInterceptLoad` | 434 | WebContent -> UI | stream |
| `LogStream_WebResourceLoaderDidReceiveResponseNotContinuingLoad` | 435 | WebContent -> UI | stream |
| `LogStream_WebResourceLoaderServiceWorkerDidNotHandle` | 436 | WebContent -> UI | stream |
| `LogStream_WebResourceLoaderStopLoadingAfterSecurityPolicyDenied` | 437 | WebContent -> UI | stream |
| `LogStream_WebResourceLoaderWillSendRequest` | 438 | WebContent -> UI | stream |
| `LogStream_WebResourceLoaderWillSendRequestContinue` | 439 | WebContent -> UI | stream |
| `LogStream_WebResourceLoaderWillSendRequestNoCoreLoader` | 440 | WebContent -> UI | stream |
| `MediaPlayerPrivateRemote_CreateResourceLoader` | 450 | GPU -> WebContent |  |
| `MediaPlayerPrivateRemote_DestroyResourceLoader` | 453 | GPU -> WebContent |  |
| `ModelProcessModelPlayer_DidConvertModelData` | 522 | Model -> WebContent |  |
| `NetworkConnectionToWebProcess_CountWebSocketChannelsForTesting` | 565 | WebContent -> Networking | async reply |
| `NetworkConnectionToWebProcess_DropNonSerializableInProcessCache` | 575 | WebContent -> Networking |  |
| `NetworkProcessConnection_DropNonSerializableInProcessCache` | 678 | Networking -> WebContent |  |
| `NetworkProcessProxy_ConsiderProcessSwapForNavigationResponse` | 684 | Networking -> UI | async reply |
| `NetworkProcessProxy_DidPerformEvictionForDomains` | 704 | Networking -> UI |  |
| `NetworkProcessProxy_ReceivedMainResourceResponseWithCertificateInfo` | 725 | Networking -> UI |  |
| `NetworkProcess_AddAllowedWebPageProxyIdentifier` | 753 | UI -> Networking |  |
| `NetworkProcess_CanPrefetchDNSForTesting` | 767 | UI -> Networking | async reply |
| `NetworkProcess_ClearCrossOriginPreflightResultCacheForTesting` | 4354 | UI -> Networking | sync |
| `NetworkProcess_FlushNetworkProcessIPC` | 833 | UI -> Networking | async reply |
| `NetworkProcess_InstallMockParentalControlsURLFilterForTesting` | 867 | UI -> Networking | async reply |
| `NetworkProcess_IsEnhancedSecurityLink` | 869 | UI -> Networking | async reply |
| `NetworkProcess_PrefetchedDNSHostnameCountForTesting` | 904 | UI -> Networking | async reply |
| `NetworkProcess_RecordMessagePortTransferDestinationsForSiteIsolation` | 914 | UI -> Networking | async reply |
| `NetworkProcess_SetCORSDisablingPatternsForPage` | 955 | UI -> Networking |  |
| `NetworkProcess_SetWebProcessSuspended` | 1049 | UI -> Networking |  |
| `NetworkStorageManager_AddGlobalIdentifierReference` | 1091 | WebContent -> Networking |  |
| `NetworkStorageManager_RemoveGlobalIdentifierReferences` | 1175 | WebContent -> Networking |  |
| `NetworkStorageManager_ResolveGlobalIdentifier` | 1184 | WebContent -> Networking | async reply |
| `PlatformXRSystemProxy_SessionDidInitializeRendering` | 1226 | UI -> WebContent |  |
| `ProxyingNetworkAgent_DataReceived` | 1288 | WebContent -> UI |  |
| `ProxyingNetworkAgent_LoadingFailed` | 1289 | WebContent -> UI |  |
| `ProxyingNetworkAgent_LoadingFinished` | 1290 | WebContent -> UI |  |
| `ProxyingNetworkAgent_RequestServedFromMemoryCache` | 1291 | WebContent -> UI |  |
| `ProxyingNetworkAgent_RequestWillBeSent` | 1292 | WebContent -> UI |  |
| `ProxyingNetworkAgent_ResponseReceived` | 1293 | WebContent -> UI |  |
| `ProxyingPageAgent_DomContentEventFired` | 1294 | WebContent -> UI |  |
| `ProxyingPageAgent_FrameDetached` | 1295 | WebContent -> UI |  |
| `ProxyingPageAgent_FrameNavigated` | 1296 | WebContent -> UI |  |
| `ProxyingPageAgent_LoadEventFired` | 1297 | WebContent -> UI |  |
| `PushClientConnection_GetAllPushSubscriptionOrigins` | 1299 | Unknown -> Unknown | async reply |
| `RemoteAudioSourceProviderManager_SetNeedsFlush` | 1387 | GPU -> WebContent |  |
| `RemoteAudioSourceProviderManager_SetPlaybackRate` | 1388 | GPU -> WebContent |  |
| `RemoteAudioSourceProviderManager_SetPreservesPitch` | 1389 | GPU -> WebContent |  |
| `RemoteAudioSourceProviderManager_SetVolume` | 1390 | GPU -> WebContent |  |
| `RemoteAudioVideoRendererProxyManager_CurrentBitmapImage` | 1397 | WebContent -> GPU | async reply |
| `RemoteAudioVideoRendererProxyManager_FinishSeek` | 1402 | WebContent -> GPU | async reply |
| `RemoteAudioVideoRendererProxyManager_SetScreenReserved` | 1436 | WebContent -> GPU |  |
| `RemoteAudioVideoRendererProxyManager_SetVideoLayerSize` | 1441 | WebContent -> GPU |  |
| `RemoteAudioVideoRendererProxyManager_SetVideoPlaybackMetricsUpdateInterval` | 1443 | WebContent -> GPU |  |
| `RemoteBuffer_GenerateAValidationError` | 1459 | WebContent -> GPU | stream |
| `RemoteGPU_CreateModelBacking` | 4374 | WebContent -> GPU | sync, stream |
| `RemoteGraphicsContextGL_ActiveAttribs` | 4377 | WebContent -> GPU | sync, stream |
| `RemoteGraphicsContextGL_ActiveUniforms` | 4378 | WebContent -> GPU | sync, stream |
| `RemoteGraphicsContext_ClipCachedPath` | 1791 | WebContent -> GPU | stream |
| `RemoteGraphicsContext_FillCachedPath` | 1821 | WebContent -> GPU | stream |
| `RemoteGraphicsContext_StrokeLinesWithColorAndThickness` | 1880 | WebContent -> GPU | stream |
| `RemoteImageBufferSet_SubmitDrawingCommands` | 1889 | WebContent -> GPU | stream |
| `RemoteLayerTreeDrawingAreaProxy_NotifyFlushingLayerTree` | 1903 | WebContent -> UI |  |
| `RemoteMediaPlayerProxy_BitmapImageForCurrentTime` | 1924 | WebContent -> GPU | async reply |
| `RemoteMediaPlayerProxy_SetViewportVisibility` | 1977 | WebContent -> GPU |  |
| `RemoteMediaResourceLoaderProxy_RemoveResource` | 1989 | GPU -> WebContent | async reply |
| `RemoteMediaResourceLoaderProxy_RequestResource` | 1991 | GPU -> WebContent |  |
| `RemoteMediaResourceLoaderProxy_SendH2Ping` | 1992 | GPU -> WebContent | async reply |
| `RemoteMediaResourceLoader_AccessControlCheckFailed` | 1994 | WebContent -> GPU |  |
| `RemoteMediaResourceLoader_DataReceived` | 1995 | WebContent -> GPU | async reply |
| `RemoteMediaResourceLoader_DataSent` | 1997 | WebContent -> GPU |  |
| `RemoteMediaResourceLoader_LoadFailed` | 1998 | WebContent -> GPU |  |
| `RemoteMediaResourceLoader_LoadFinished` | 1999 | WebContent -> GPU |  |
| `RemoteMediaResourceLoader_RedirectReceived` | 2000 | WebContent -> GPU | async reply |
| `RemoteMediaResourceLoader_ResponseReceived` | 2002 | WebContent -> GPU | async reply |
| `RemoteMesh_Destruct` | 2059 | WebContent -> GPU | stream |
| `RemoteMesh_PaintCurrentFrameToImageBuffer` | 4463 | WebContent -> GPU | sync, stream |
| `RemoteMesh_Play` | 2060 | WebContent -> GPU | stream |
| `RemoteMesh_ProcessRemovals` | 2061 | WebContent -> GPU | stream, async reply |
| `RemoteMesh_Render` | 2063 | WebContent -> GPU | stream, async reply |
| `RemoteMesh_SetEnvironmentMap` | 2065 | WebContent -> GPU | stream |
| `RemoteMesh_SetFOV` | 2066 | WebContent -> GPU | stream |
| `RemoteMesh_SetLabel` | 2067 | WebContent -> GPU | stream |
| `RemoteMesh_Update` | 2068 | WebContent -> GPU | stream, async reply |
| `RemoteMesh_UpdateContentsHeadroom` | 2069 | WebContent -> GPU | stream |
| `RemoteMesh_UpdateMaterial` | 2070 | WebContent -> GPU | stream, async reply |
| `RemoteMesh_UpdateRenderBuffers` | 2072 | WebContent -> GPU | stream, async reply |
| `RemoteMesh_UpdateTexture` | 2075 | WebContent -> GPU | stream, async reply |
| `RemoteMesh_UpdateTransform` | 2077 | WebContent -> GPU | stream |
| `RemoteRenderingBackend_CachePathImpl` | 2155 | WebContent -> GPU | stream |
| `RemoteRenderingBackend_ReleasePathImpl` | 2182 | WebContent -> GPU | stream |
| `SampleBufferDisplayLayer_UpdateVideoFrameCounters` | 2274 | GPU -> WebContent |  |
| `WasmDebuggerDispatcher_ResetServer` | 2379 | UI -> WebContent |  |
| `WebAutomationSessionProxy_EnsureRealmForInitialEmptyDocument` | 2402 | UI -> WebContent |  |
| `WebAutomationSessionProxy_EvaluateBidiScript` | 2403 | UI -> WebContent | async reply |
| `WebAutomationSession_ScriptRealmCreated` | 2432 | WebContent -> UI |  |
| `WebAutomationSession_ScriptRealmDestroyed` | 2433 | WebContent -> UI |  |
| `WebBackForwardList_BackForwardItemAtIndexForWebContent` | 4472 | WebContent -> UI | sync |
| `WebExtensionContext_DidEncounterScriptError` | 2570 | WebContent -> UI |  |
| `WebExtensionContext_TabsMove` | 2661 | WebContent -> UI | async reply |
| `WebFrameProxy_DidChangeCSPOriginsThatUpgradeInsecureNavigations` | 2710 | WebContent -> UI |  |
| `WebFrameProxy_FindFocusableElementContinuingFromFrame` | 2711 | WebContent -> UI |  |
| `WebFrame_FindFocusableElementContinuingFromFrame` | 2721 | UI -> WebContent |  |
| `WebFrame_RequestContainerJSHandleForExtractedText` | 2732 | UI -> WebContent | async reply |
| `WebFrame_RequestContainerJSHandleForSearchTexts` | 2734 | UI -> WebContent | async reply |
| `WebInspectorBackend_DisableNetworkInstrumentation` | 2802 | UI -> WebContent |  |
| `WebInspectorBackend_DisablePageInstrumentation` | 2803 | UI -> WebContent |  |
| `WebInspectorBackend_EnableNetworkInstrumentation` | 2804 | UI -> WebContent |  |
| `WebInspectorBackend_EnablePageInstrumentation` | 2805 | UI -> WebContent |  |
| `WebInspectorBackend_GetFrameResourceData` | 2806 | UI -> WebContent | async reply |
| `WebInspectorBackend_GetResponseBody` | 2808 | UI -> WebContent | async reply |
| `WebInspectorUI_SystemAppearanceDidChange` | 2887 | Unknown -> WebContent |  |
| `WebPageProxy_AddResourceTimingFromSubframe` | 2904 | WebContent -> UI |  |
| `WebPageProxy_AddTextEffectForID` | 2908 | WebContent -> UI |  |
| `WebPageProxy_ApplyMonitorUnloadToFrameOwner` | 2909 | WebContent -> UI |  |
| `WebPageProxy_DidCacheBackForwardItem` | 2940 | WebContent -> UI | async reply |
| `WebPageProxy_DidConsumeUserActivation` | 2954 | WebContent -> UI |  |
| `WebPageProxy_DidEvictBackForwardItem` | 2962 | WebContent -> UI |  |
| `WebPageProxy_DidNotifyUserActivation` | 2981 | WebContent -> UI |  |
| `WebPageProxy_DidTakeBackForwardItemForRestoration` | 3000 | WebContent -> UI |  |
| `WebPageProxy_DismissDigitalCredentialsChooser` | 3006 | WebContent -> UI | async reply |
| `WebPageProxy_DispatchCrossOriginBeforeUnloadCheckForFrame` | 3008 | WebContent -> UI |  |
| `WebPageProxy_GetLoadDecisionForIcons` | 3031 | WebContent -> UI |  |
| `WebPageProxy_GoToBackForwardItemAtIndex` | 3032 | WebContent -> UI |  |
| `WebPageProxy_PropagateDragAndDrop` | 3073 | WebContent -> UI |  |
| `WebPageProxy_RemoveTextEffectForID` | 3088 | WebContent -> UI |  |
| `WebPageProxy_RequestFrameScreenPosition` | 3093 | WebContent -> UI |  |
| `WebPageProxy_ScheduleAccessibilityFrameGeometryUpdate` | 3118 | WebContent -> UI |  |
| `WebPageProxy_SetAccessibilityMode` | 3123 | WebContent -> UI |  |
| `WebPageProxy_SetPDFDisplayMode` | 3139 | WebContent -> UI |  |
| `WebPageProxy_SetWindowFrameIPC` | 3144 | WebContent -> UI |  |
| `WebPageProxy_ShowDigitalCredentialsChooser` | 3158 | WebContent -> UI | async reply |
| `WebPageProxy_ShowWritingToolsAffordance` | 3170 | WebContent -> UI |  |
| `WebPageProxy_TranscodeChosenFiles` | 3188 | WebContent -> UI | async reply |
| `WebPageProxy_UpdateRemoteFrameAccessibilityInheritedState` | 3196 | WebContent -> UI |  |
| `WebPageProxy_UpdateRemoteIntersectionObserversInOtherWebProcesses` | 3198 | WebContent -> UI |  |
| `WebPageTesting_NumberOfLiveDocuments` | 3222 | UI -> WebContent | async reply |
| `WebPageTesting_StartMonitoringWheelEventsForTesting` | 3230 | UI -> WebContent | async reply |
| `WebPageTesting_WaitForWheelEventsToCompleteForTesting` | 3232 | UI -> WebContent | async reply |
| `WebPage_AddResourceTimingFromSubframe` | 3240 | Unknown -> WebContent |  |
| `WebPage_ApplyMonitorUnloadToIFrameElement` | 3255 | Unknown -> WebContent |  |
| `WebPage_ClearContentWorld` | 3278 | Unknown -> WebContent | async reply |
| `WebPage_ClearDeviceOrientationAndMotionPermissions` | 3280 | Unknown -> WebContent |  |
| `WebPage_ClearDictationStreamingOpacity` | 3282 | Unknown -> WebContent |  |
| `WebPage_ConsumeUserActivations` | 3303 | Unknown -> WebContent |  |
| `WebPage_ContentsToRootViewRects` | 3309 | Unknown -> WebContent | async reply |
| `WebPage_CreateTextIndicatorForTextEffectID` | 3325 | Unknown -> WebContent | async reply |
| `WebPage_DispatchCrossOriginBeforeUnloadCheckForFrame` | 3373 | Unknown -> WebContent |  |
| `WebPage_GetFrameTreeForBackForwardCacheEntry` | 3461 | Unknown -> WebContent | async reply |
| `WebPage_GetImageMetadata` | 3465 | Unknown -> WebContent | async reply |
| `WebPage_InheritAccessibilityMode` | 3526 | Unknown -> WebContent |  |
| `WebPage_InvalidateBackForwardListCache` | 3539 | Unknown -> WebContent |  |
| `WebPage_IsMarkedTextRequiredForComposition` | 3540 | Unknown -> WebContent | async reply |
| `WebPage_KeepBlobURLAliveForNewWindowNavigation` | 3542 | Unknown -> WebContent | handled during sync waits |
| `WebPage_ReleaseKeptBlobURLForNewWindowNavigation` | 3603 | Unknown -> WebContent |  |
| `WebPage_RequestPDFDisplayMode` | 3645 | Unknown -> WebContent |  |
| `WebPage_RestoreWithFrameItem` | 3660 | Unknown -> WebContent | async reply |
| `WebPage_SelectLastFoundRange` | 3676 | Unknown -> WebContent | async reply |
| `WebPage_SetDictationStreamingOpacity` | 3714 | Unknown -> WebContent |  |
| `WebPage_SetDisplayCaptureEnvironment` | 3715 | Unknown -> WebContent |  |
| `WebPage_SetMediaPlaybackEnvironment` | 3741 | Unknown -> WebContent |  |
| `WebPage_SetWritingToolsAvailable` | 3782 | Unknown -> WebContent |  |
| `WebPage_SuspendWithFrameItem` | 3817 | Unknown -> WebContent | async reply |
| `WebPage_TakeRemoteSnapshot` | 3822 | Unknown -> WebContent | async reply |
| `WebPage_UpdateRemoteIntersectionObservers` | 3854 | Unknown -> WebContent |  |
| `WebPage_UpdateRemotePageAccessibilityInheritedState` | 3855 | Unknown -> WebContent |  |
| `WebPage_UpdateRemotePageAccessibilityScreenPosition` | 3857 | Unknown -> WebContent |  |
| `WebPage_UpdateUnderlyingTextVisibilityForTextEffectID` | 3873 | Unknown -> WebContent | async reply |
| `WebPage_UpdateUserActivationState` | 3875 | Unknown -> WebContent |  |
| `WebProcessProxy_CacheMediaSourceTypeSupported` | 3943 | WebContent -> UI |  |
| `WebProcess_GetStorageAreaMapCountForTesting` | 4012 | UI -> WebContent | async reply |
| `WebProcess_SetMediaAccessibilityPreferredCaptionDisplayMode` | 4078 | UI -> WebContent |  |
| `WebProcess_SetMediaAccessibilityPreferredLanguages` | 4079 | UI -> WebContent |  |
| `WebProcess_UpdateConsistentPrivacyQuirkFilter` | 4096 | UI -> WebContent |  |
| `WebResourceLoader_SetServiceWorkerTimingInfo` | 4115 | Networking -> WebContent |  |

## Removed (315)

| Message | Number | Route | Flags |
| --- | --- | --- | --- |
| `AudioVideoRendererRemoteMessageReceiver_StallTimeReached` | 12 | GPU -> WebContent |  |
| `GPUConnectionToWebProcess_EnableMockMediaSource` | 69 | WebContent -> GPU |  |
| `GPUConnectionToWebProcess_SetMediaEnvironment` | 76 | WebContent -> GPU |  |
| `GPUProcess_RequestBitmapImageForCurrentTime` | 110 | UI -> GPU | async reply |
| `IPCTesterReceiverSwift_AsyncMessage` | 141 | Unknown -> Unknown | async reply |
| `LogStream_DOCUMENTLOADER_ATTACHTOFRAME` | 204 | WebContent -> UI | stream |
| `LogStream_DOCUMENTLOADER_DETACHFROMFRAME` | 205 | WebContent -> UI | stream |
| `LogStream_DOCUMENTLOADER_STARTLOADINGMAINRESOURCE_EMTPY_DOCUMENT` | 206 | WebContent -> UI | stream |
| `LogStream_DOCUMENTLOADER_STARTLOADINGMAINRESOURCE_STARTING_LOAD` | 207 | WebContent -> UI | stream |
| `LogStream_DOCUMENTLOADER_STOPLOADING` | 208 | WebContent -> UI | stream |
| `LogStream_FONTCACHECORETEXT_REGISTER_ERROR` | 209 | WebContent -> UI | stream |
| `LogStream_FONTCACHECORETEXT_REGISTER_FONT` | 210 | WebContent -> UI | stream |
| `LogStream_FRAMELOADER_CHANGELOCATION` | 211 | WebContent -> UI | stream |
| `LogStream_FRAMELOADER_CHECKLOADCOMPLETEFORTHISFRAME` | 212 | WebContent -> UI | stream |
| `LogStream_FRAMELOADER_CONTINUELOADAFTERNAVIGATIONPOLICY` | 213 | WebContent -> UI | stream |
| `LogStream_FRAMELOADER_CONTINUELOADAFTERNAVIGATIONPOLICY_CANNOT_CONTINUE` | 214 | WebContent -> UI | stream |
| `LogStream_FRAMELOADER_LOADFRAMEREQUEST_FRAME_LOAD_STARTED` | 215 | WebContent -> UI | stream |
| `LogStream_FRAMELOADER_LOADURLINTOCHILDFRAME` | 216 | WebContent -> UI | stream |
| `LogStream_FRAMELOADER_LOADWITHDOCUMENTLOADER_FRAME_LOAD_STARTED` | 217 | WebContent -> UI | stream |
| `LogStream_FRAMELOADER_LOADWITHDOCUMENTLOADER_MAIN_FRAME_LOAD_STARTED` | 218 | WebContent -> UI | stream |
| `LogStream_FRAMELOADER_LOADWITHNAVIGATIONACTION` | 219 | WebContent -> UI | stream |
| `LogStream_FRAMELOADER_LOAD_DOCUMENTLOADER` | 220 | WebContent -> UI | stream |
| `LogStream_FRAMELOADER_LOAD_FRAMELOADREQUEST` | 221 | WebContent -> UI | stream |
| `LogStream_FRAMELOADER_LOAD_URL` | 222 | WebContent -> UI | stream |
| `LogStream_FRAMELOADER_PREPAREFORLOADSTART` | 223 | WebContent -> UI | stream |
| `LogStream_FRAMELOADER_RELOAD` | 224 | WebContent -> UI | stream |
| `LogStream_FRAMELOADER_SETDOCUMENTLOADER` | 225 | WebContent -> UI | stream |
| `LogStream_FRAMELOADER_SETPOLICYDOCUMENTLOADER` | 226 | WebContent -> UI | stream |
| `LogStream_FRAMELOADER_SETPROVISIONALDOCUMENTLOADER` | 227 | WebContent -> UI | stream |
| `LogStream_FRAMELOADER_SETSTATE_MAIN_FRAME_LOAD_COMPLETED` | 228 | WebContent -> UI | stream |
| `LogStream_FRAMELOADER_STOPALLLOADERS` | 229 | WebContent -> UI | stream |
| `LogStream_FRAMELOADER_STOPALLLOADERS_CLEARING_PROVISIONAL_DOCUMENT_LOADER` | 230 | WebContent -> UI | stream |
| `LogStream_FRAMELOADER_TRANSITIONTOCOMMITTED` | 231 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_ADDAUDIOTRACK` | 232 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_ADDVIDEOTRACK` | 233 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_CANPLAYTYPE` | 234 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_CANTRANSITIONFROMAUTOPLAYTOPLAY_NOT_AUTOPLAYING` | 235 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_CANTRANSITIONFROMAUTOPLAYTOPLAY_NOT_ENOUGH_DATA` | 236 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_CONFIGURETEXTTRACKDISPLAY` | 237 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_CONFIGURETEXTTRACKGROUP` | 238 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_CONSTRUCTOR` | 239 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_CREATEMEDIAPLAYER` | 240 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_CURRENTMEDIATIME_SEEKING` | 241 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_DESTRUCTOR` | 242 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_DIDFINISHINSERTINGNODE` | 243 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_INSERTEDINTOANCESTOR` | 244 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_MEDIAENGINEWASUPDATED` | 245 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_MEDIAPLAYERCHARACTERISTICSCHANGED` | 246 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_MEDIAPLAYERCHARACTERISTICSCHANGED_NO_MEDIASESSION` | 247 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_MEDIAPLAYERDURATIONCHANGED` | 248 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_MEDIAPLAYERENGINEUPDATED` | 249 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_MEDIAPLAYERRATECHANGED` | 250 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_MEDIAPLAYERSIZECHANGED` | 251 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_MEDIAPLAYERTIMECHANGED` | 252 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_PAUSE` | 253 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_PAUSEINTERNAL` | 254 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_PLAY` | 255 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_PLAYINTERNAL` | 256 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_PREPAREFORLOAD` | 257 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_REMOVEAUDIOTRACK` | 258 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_REMOVEDFROMANCESTOR` | 259 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_SCENEIDENTIFIERDIDCHANGE` | 260 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_SCHEDULECONFIGURETEXTTRACKS_LAMBDA_TASK_FIRED` | 261 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_SCHEDULECONFIGURETEXTTRACKS_TASK_SCHEDULED` | 262 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_SCHEDULEMEDIAENGINEWASUPDATED_LAMBDA_TASK_FIRED` | 263 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_SCHEDULEMEDIAENGINEWASUPDATED_TASK_SCHEDULED` | 264 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_SELECTMEDIARESOURCE_ATTEMPTING_USE_OF_UNATTACHED_MEDIASOURCEHANDLE` | 265 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_SELECTMEDIARESOURCE_EMPTY_SRC` | 266 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_SELECTMEDIARESOURCE_HAS_SRCATTR_PLAYER_NOT_CREATED` | 267 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_SELECTMEDIARESOURCE_LAMBDA_TASK_FIRED` | 268 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_SELECTMEDIARESOURCE_NOTHING_TO_LOAD` | 269 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_SELECTMEDIARESOURCE_USING_SRCOBJECT_PROPERTY` | 270 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_SELECTMEDIARESOURCE_USING_SRC_ATTRIBUTE_URL` | 271 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_SETAUTOPLAYEVENTPLAYBACKSTATE` | 272 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_SETBUFFERINGPOLICY` | 273 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_SETMUTEDINTERNAL` | 274 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_SETNETWORKSTATE` | 275 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_SETPLAYBACKRATE` | 276 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_SETREADYSTATE` | 277 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_SETSHOULDDELAYLOADEVENT` | 278 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_SETSHOWPOSTERFLAG` | 279 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_SETVOLUME` | 280 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_UPDATEPLAYSTATE` | 281 | WebContent -> UI | stream |
| `LogStream_HTMLMEDIAELEMENT_VISIBILITYSTATECHANGED` | 282 | WebContent -> UI | stream |
| `LogStream_HTMLVIDEOELEMENT_MEDIAPLAYERFIRSTVIDEOFRAMEAVAILABLE` | 283 | WebContent -> UI | stream |
| `LogStream_HTMLVIDEOELEMENT_MEDIAPLAYERRENDERINGMODECHANGED` | 284 | WebContent -> UI | stream |
| `LogStream_HTMLVIDEOELEMENT_SCHEDULERESIZEEVENT` | 285 | WebContent -> UI | stream |
| `LogStream_LIBWEBRTCMEDIAENDPOINT_ONSTATSDELIVERED` | 286 | WebContent -> UI | stream |
| `LogStream_LIBWEBRTC_LOG_ERROR` | 287 | WebContent -> UI | stream |
| `LogStream_LIBWEBRTC_LOG_MESSAGE` | 288 | WebContent -> UI | stream |
| `LogStream_LOCALFRAMEVIEW_FIRING_FIRST_VISUALLY_NON_EMPTY_LAYOUT_MILESTONE` | 289 | WebContent -> UI | stream |
| `LogStream_LOCALFRAMEVIEW_FIRING_RESIZE_EVENTS_DISABLED_FOR_PAGE` | 290 | WebContent -> UI | stream |
| `LogStream_LOCALFRAMEVIEW_NOT_PAINTING_LAYOUT_NEEDED` | 291 | WebContent -> UI | stream |
| `LogStream_MEDIAPLAYERPRIVATEREMOTE_LAYERHOSTINGCONTEXTCHANGED` | 293 | WebContent -> UI | stream |
| `LogStream_MEDIASESSIONMANAGERCOCOA_CLIENTCHARACTERISTICSCHANGED` | 294 | WebContent -> UI | stream |
| `LogStream_MEDIASESSIONMANAGERCOCOA_SESSIONCANPRODUCEAUDIOCHANGED` | 295 | WebContent -> UI | stream |
| `LogStream_MEDIASESSIONMANAGERCOCOA_UPDATESESSIONSTATE` | 296 | WebContent -> UI | stream |
| `LogStream_MEDIASESSIONMANAGERINTERFACE_ADDSESSION` | 297 | WebContent -> UI | stream |
| `LogStream_MEDIASESSIONMANAGERINTERFACE_MAYBEACTIVATEAUDIOSESSION_ACTIVE_SESSION_NOT_REQUIRED` | 298 | WebContent -> UI | stream |
| `LogStream_MEDIASESSIONMANAGERINTERFACE_REMOVESESSION` | 299 | WebContent -> UI | stream |
| `LogStream_MEDIASESSIONMANAGERINTERFACE_SESSIONCANPRODUCEAUDIOCHANGED` | 300 | WebContent -> UI | stream |
| `LogStream_MEDIASESSIONMANAGERINTERFACE_SESSIONWILLENDPLAYBACK` | 301 | WebContent -> UI | stream |
| `LogStream_PEERCONNECTIONBACKEND_CREATEANSWERSUCCEEDED` | 302 | WebContent -> UI | stream |
| `LogStream_PEERCONNECTIONBACKEND_CREATEOFFERSUCCEEDED` | 303 | WebContent -> UI | stream |
| `LogStream_PERFORMANCELOGGING_MEMORY_USAGE_FOR_KEY` | 304 | WebContent -> UI | stream |
| `LogStream_PERFORMANCELOGGING_MEMORY_USAGE_INFO` | 305 | WebContent -> UI | stream |
| `LogStream_PERFORMANCEMONITOR_MEASURE_CPUUSAGE_IN_ACTIVITYSTATE` | 306 | WebContent -> UI | stream |
| `LogStream_PERFORMANCEMONITOR_MEASURE_POSTBACKGROUND_CPUUSAGE` | 307 | WebContent -> UI | stream |
| `LogStream_PERFORMANCEMONITOR_MEASURE_POSTBACKGROUND_MEMORYUSAGE` | 308 | WebContent -> UI | stream |
| `LogStream_PERFORMANCEMONITOR_MEASURE_POSTLOAD_CPUUSAGE` | 309 | WebContent -> UI | stream |
| `LogStream_PERFORMANCEMONITOR_MEASURE_POSTLOAD_MEMORYUSAGE` | 310 | WebContent -> UI | stream |
| `LogStream_PLATFORM_INITIALIZE_WEBPROCESS` | 311 | WebContent -> UI | stream |
| `LogStream_POLICYCHECKER_CHECKNAVIGATIONPOLICY_CONTINUE_INITIAL_EMPTY_DOCUMENT` | 312 | WebContent -> UI | stream |
| `LogStream_POLICYCHECKER_CHECKNAVIGATIONPOLICY_CONTINUE_LOAD_IN_ANOTHER_PROCESS` | 313 | WebContent -> UI | stream |
| `LogStream_PROGRESSTRACKER_FINALPROGRESSCOMPLETE` | 314 | WebContent -> UI | stream |
| `LogStream_PROGRESSTRACKER_PROGRESSCOMPLETED` | 315 | WebContent -> UI | stream |
| `LogStream_PROGRESSTRACKER_PROGRESSSTARTED` | 316 | WebContent -> UI | stream |
| `LogStream_RECEIVED_LAUNCH_SERVICES_DATABASE` | 317 | WebContent -> UI | stream |
| `LogStream_REMOTE_RENDERING_BACKEND_PROXY_CREATED_RENDERING_BACKEND` | 318 | WebContent -> UI | stream |
| `LogStream_RESOURCELOADER_WILLSENDREQUESTINTERNAL` | 319 | WebContent -> UI | stream |
| `LogStream_RTCPEERCONNECTION_SETLOCALDESCRIPTION` | 320 | WebContent -> UI | stream |
| `LogStream_RTCPEERCONNECTION_SETREMOTEDESCRIPTION` | 321 | WebContent -> UI | stream |
| `LogStream_SERVICEWORKERTHREADPROXY_REMOVEFETCH` | 322 | WebContent -> UI | stream |
| `LogStream_SUBRESOURCELOADER_DIDFAIL` | 323 | WebContent -> UI | stream |
| `LogStream_SUBRESOURCELOADER_DIDFINISHLOADING` | 324 | WebContent -> UI | stream |
| `LogStream_SUBRESOURCELOADER_DIDFINISHLOADING_CANCELED` | 325 | WebContent -> UI | stream |
| `LogStream_SUBRESOURCELOADER_DIDFINISHLOADING_DID_NOT_REACH_TERMINAL_STATE` | 326 | WebContent -> UI | stream |
| `LogStream_SUBRESOURCELOADER_DIDFINISHLOADING_REACHED_TERMINAL_STATE` | 327 | WebContent -> UI | stream |
| `LogStream_SUBRESOURCELOADER_DIDRECEIVERESPONSE_CANCELING_LOAD_BECAUSE_OF_CROSS_ORIGIN_ACCESS_CONTROL` | 328 | WebContent -> UI | stream |
| `LogStream_SUBRESOURCELOADER_DIDRECEIVERESPONSE_CANCELING_LOAD_BECAUSE_OF_MULTIPART_NON_IMAGE` | 329 | WebContent -> UI | stream |
| `LogStream_SUBRESOURCELOADER_DIDRECEIVERESPONSE_CANCELING_LOAD_BLOCKED_BY_CONTENT_POLICY` | 330 | WebContent -> UI | stream |
| `LogStream_SUBRESOURCELOADER_DIDRECEIVERESPONSE_CANCELING_LOAD_RECEIVED_UNEXPECTED_RANGE_RESPONSE` | 331 | WebContent -> UI | stream |
| `LogStream_SUBRESOURCELOADER_WILLCANCEL` | 332 | WebContent -> UI | stream |
| `LogStream_SUBRESOURCELOADER_WILLSENDREQUESTINTERNAL` | 333 | WebContent -> UI | stream |
| `LogStream_SUBRESOURCELOADER_WILLSENDREQUESTINTERNAL_CANCELLED_INVALID_NEW_REQUEST` | 334 | WebContent -> UI | stream |
| `LogStream_SUBRESOURCELOADER_WILLSENDREQUESTINTERNAL_CANCELLED_INVALID_REQUEST` | 335 | WebContent -> UI | stream |
| `LogStream_SUBRESOURCELOADER_WILLSENDREQUESTINTERNAL_CANCELLED_TERMINAL_STATE` | 336 | WebContent -> UI | stream |
| `LogStream_SUBRESOURCELOADER_WILLSENDREQUESTINTERNAL_REACHED_TERMINAL_STATE` | 337 | WebContent -> UI | stream |
| `LogStream_SUBRESOURCELOADER_WILLSENDREQUESTINTERNAL_RESOURCELOAD_CANCELLED_REDIRECT_NOT_ALLOWED` | 338 | WebContent -> UI | stream |
| `LogStream_SUBRESOURCELOADER_WILLSENDREQUESTINTERNAL_RESOURCELOAD_FINISHED` | 339 | WebContent -> UI | stream |
| `LogStream_SUBRESOURCELOADER_WILLSENDREQUESTINTERNAL_RESOURCE_DONE_NOTIFYING_CLIENTS` | 340 | WebContent -> UI | stream |
| `LogStream_SUBRESOURCELOADER_WILLSENDREQUESTINTERNAL_RESOURCE_LOAD_CANCELLED_AFTER_IMAGE_BEING_DEFERRED` | 341 | WebContent -> UI | stream |
| `LogStream_SUBRESOURCELOADER_WILLSENDREQUESTINTERNAL_RESOURCE_LOAD_CANCELLED_AFTER_REDIRECT_DENIED_BY_CORS_POLICY` | 342 | WebContent -> UI | stream |
| `LogStream_SUBRESOURCELOADER_WILLSENDREQUESTINTERNAL_RESOURCE_LOAD_CANCELLED_AFTER_USING_BLOCKED_PORT` | 343 | WebContent -> UI | stream |
| `LogStream_SUBRESOURCELOADER_WILLSENDREQUESTINTERNAL_RESOURCE_LOAD_CANCELLED_CANNOT_REQUEST_AFTER_REDIRECTION` | 344 | WebContent -> UI | stream |
| `LogStream_SUBRESOURCELOADER_WILLSENDREQUESTINTERNAL_RESOURCE_LOAD_CANCELLED_TOO_MANY_REDIRECTS` | 345 | WebContent -> UI | stream |
| `LogStream_SUBRESOURCELOADER_WILLSENDREQUESTINTERNAL_RESOURCE_LOAD_COMPLETED` | 346 | WebContent -> UI | stream |
| `LogStream_SUBRESOURCELOADER_WILLSENDREQUESTINTERNAL_TERMINAL_STATE_CALLING_COMPLETION_HANDLER` | 347 | WebContent -> UI | stream |
| `LogStream_TIMED_OUT_WAITING_FOR_LAUNCH_SERVICES_DATABASE_UPDATE` | 348 | WebContent -> UI | stream |
| `LogStream_VIDEOPRESENTATIONMANAGER_SETVIDEOLAYERFRAMEFENCED` | 349 | WebContent -> UI | stream |
| `LogStream_WAITING_FOR_LAUNCH_SERVICES_DATABASE_UPDATE_TOOK_F_SECONDS` | 350 | WebContent -> UI | stream |
| `LogStream_WEBCORE_TEST_LOG` | 351 | WebContent -> UI | stream |
| `LogStream_WEBFRAMELOADERCLIENT_DISPATCHDECIDEPOLICYFORNAVIGATIONACTION_GOT_POLICYACTION_FROM_ASYNC_IPC` | 352 | WebContent -> UI | stream |
| `LogStream_WEBFRAMELOADERCLIENT_DISPATCHDECIDEPOLICYFORNAVIGATIONACTION_GOT_POLICYACTION_FROM_SYNC_IPC` | 353 | WebContent -> UI | stream |
| `LogStream_WEBFRAMELOADERCLIENT_DISPATCHDECIDEPOLICYFORNAVIGATIONACTION_SYNC_IPC_FAILED` | 354 | WebContent -> UI | stream |
| `LogStream_WEBFRAMELOADERCLIENT_NAVIGATIONACTIONDATA_EMPTY_REQUEST` | 355 | WebContent -> UI | stream |
| `LogStream_WEBFRAMELOADERCLIENT_NAVIGATIONACTIONDATA_NO_FRAME` | 356 | WebContent -> UI | stream |
| `LogStream_WEBFRAMELOADERCLIENT_NAVIGATIONACTIONDATA_NO_WEBPAGE` | 357 | WebContent -> UI | stream |
| `LogStream_WEBLOADERSTRATEGY_SCHEDULELOAD` | 358 | WebContent -> UI | stream |
| `LogStream_WEBLOADERSTRATEGY_SCHEDULELOAD_RESOURCE_SCHEDULED_WITH_NETWORKPROCESS` | 359 | WebContent -> UI | stream |
| `LogStream_WEBLOADERSTRATEGY_SCHEDULELOAD_URL_LOADED_AS_DATA` | 360 | WebContent -> UI | stream |
| `LogStream_WEBLOCALFRAMELOADERCLIENT_COMPLETE_PAGE_TRANSITION_IF_NEEDED` | 361 | WebContent -> UI | stream |
| `LogStream_WEBLOCALFRAMELOADERCLIENT_DISPATCH_DID_FIRST_LAYOUT_FOR_FRAME` | 362 | WebContent -> UI | stream |
| `LogStream_WEBLOCALFRAMELOADERCLIENT_DISPATCH_DID_FIRST_VISUALLY_NONEMPTY_LAYOUT` | 363 | WebContent -> UI | stream |
| `LogStream_WEBLOCALFRAMELOADERCLIENT_DISPATCH_DID_REACH_LAYOUT_MILESTONE` | 364 | WebContent -> UI | stream |
| `LogStream_WEBPAGE_CLOSE` | 365 | WebContent -> UI | stream |
| `LogStream_WEBPAGE_FAILED_TO_MARK_ALL_LAYERS_VOLATILE` | 366 | WebContent -> UI | stream |
| `LogStream_WEBPAGE_FREEZE_LAYER_TREE` | 367 | WebContent -> UI | stream |
| `LogStream_WEBPAGE_LOADREQUEST` | 368 | WebContent -> UI | stream |
| `LogStream_WEBPAGE_MARK_LAYERS_VOLATILE` | 369 | WebContent -> UI | stream |
| `LogStream_WEBPAGE_UNFREEZE_LAYER_TREE` | 370 | WebContent -> UI | stream |
| `LogStream_WEBPROCESS_DESTROY_RENDERING_RESOURCES` | 371 | WebContent -> UI | stream |
| `LogStream_WEBPROCESS_FREEZE_ALL_LAYER_TREES` | 372 | WebContent -> UI | stream |
| `LogStream_WEBPROCESS_MARK_ALL_LAYERS_VOLATILE` | 373 | WebContent -> UI | stream |
| `LogStream_WEBPROCESS_PREPARE_TO_SUSPEND` | 374 | WebContent -> UI | stream |
| `LogStream_WEBPROCESS_READY_TO_SUSPEND` | 375 | WebContent -> UI | stream |
| `LogStream_WEBRESOURCELOADER_CONSTRUCTOR` | 376 | WebContent -> UI | stream |
| `LogStream_WEBRESOURCELOADER_DIDBLOCKAUTHENTICATIONCHALLENGE` | 377 | WebContent -> UI | stream |
| `LogStream_WEBRESOURCELOADER_DIDFAILRESOURCELOAD` | 378 | WebContent -> UI | stream |
| `LogStream_WEBRESOURCELOADER_DIDFINISHRESOURCELOAD` | 379 | WebContent -> UI | stream |
| `LogStream_WEBRESOURCELOADER_DIDRECEIVEDATA` | 380 | WebContent -> UI | stream |
| `LogStream_WEBRESOURCELOADER_DIDRECEIVERESOURCE` | 381 | WebContent -> UI | stream |
| `LogStream_WEBRESOURCELOADER_DIDRECEIVERESOURCE_UNABLE_TO_CREATE_FRAGMENTEDSHAREDBUFFER` | 382 | WebContent -> UI | stream |
| `LogStream_WEBRESOURCELOADER_DIDRECEIVERESPONSE` | 383 | WebContent -> UI | stream |
| `LogStream_WEBRESOURCELOADER_DIDRECEIVERESPONSE_NOT_CONTINUING_INTERCEPT_LOAD` | 384 | WebContent -> UI | stream |
| `LogStream_WEBRESOURCELOADER_DIDRECEIVERESPONSE_NOT_CONTINUING_LOAD` | 385 | WebContent -> UI | stream |
| `LogStream_WEBRESOURCELOADER_SERVICEWORKERDIDNOTHANDLE` | 386 | WebContent -> UI | stream |
| `LogStream_WEBRESOURCELOADER_STOPLOADINGAFTERSECURITYPOLICYDENIED` | 387 | WebContent -> UI | stream |
| `LogStream_WEBRESOURCELOADER_WILLSENDREQUEST` | 388 | WebContent -> UI | stream |
| `LogStream_WEBRESOURCELOADER_WILLSENDREQUEST_CONTINUE` | 389 | WebContent -> UI | stream |
| `LogStream_WEBRESOURCELOADER_WILLSENDREQUEST_NO_CORELOADER` | 390 | WebContent -> UI | stream |
| `MediaPlayerPrivateRemote_ActiveSourceBuffersChanged` | 391 | GPU -> WebContent |  |
| `MediaPlayerPrivateRemote_RemoveResource` | 428 | GPU -> WebContent |  |
| `MediaPlayerPrivateRemote_RequestResource` | 431 | GPU -> WebContent |  |
| `MediaPlayerPrivateRemote_Seeked` | 433 | GPU -> WebContent |  |
| `MediaPlayerPrivateRemote_SendH2Ping` | 434 | GPU -> WebContent | async reply |
| `MediaSourcePrivateRemoteMessageReceiver_ProxyWaitForTarget` | 445 | GPU -> WebContent | async reply |
| `NetworkConnectionToWebProcess_SetCORSDisablingPatterns` | 588 | WebContent -> Networking |  |
| `NetworkProcessProxy_TriggerBrowsingContextGroupSwitchForNavigation` | 695 | Networking -> UI | async reply |
| `RemoteAudioSourceProviderManager_AudioSamplesAvailable` | 1304 | GPU -> WebContent |  |
| `RemoteAudioVideoRendererProxyManager_SeekTo` | 1330 | WebContent -> GPU | async reply |
| `RemoteDDMesh_Destruct` | 1431 | WebContent -> GPU | stream |
| `RemoteDDMesh_Play` | 1432 | WebContent -> GPU | stream |
| `RemoteDDMesh_Render` | 1433 | WebContent -> GPU | stream |
| `RemoteDDMesh_SetCameraDistance` | 1434 | WebContent -> GPU | stream |
| `RemoteDDMesh_SetLabel` | 1435 | WebContent -> GPU | stream |
| `RemoteDDMesh_Update` | 1436 | WebContent -> GPU | stream |
| `RemoteDDMesh_UpdateMaterial` | 1437 | WebContent -> GPU | stream |
| `RemoteDDMesh_UpdateTexture` | 1438 | WebContent -> GPU | stream |
| `RemoteDDMesh_UpdateTransform` | 1439 | WebContent -> GPU | stream |
| `RemoteGraphicsContextGL_GetActiveAttrib` | 4263 | WebContent -> GPU | sync, stream |
| `RemoteGraphicsContextGL_GetActiveUniform` | 4264 | WebContent -> GPU | sync, stream |
| `RemoteGraphicsContextGL_GetActiveUniforms` | 4267 | WebContent -> GPU | sync, stream |
| `RemoteGraphicsContextGL_GetAttribLocation` | 4268 | WebContent -> GPU | sync, stream |
| `RemoteGraphicsContextGL_GetUniformIndices` | 4303 | WebContent -> GPU | sync, stream |
| `RemoteGraphicsContextGL_GetUniformLocation` | 4304 | WebContent -> GPU | sync, stream |
| `RemoteGraphicsContext_StrokeLineWithColorAndThickness` | 1792 | WebContent -> GPU | stream |
| `RemoteMediaPlayerProxy_LoadMediaSource` | 1843 | WebContent -> GPU | async reply |
| `RemoteMediaPlayerProxy_NotifyActiveSourceBuffersChanged` | 1846 | WebContent -> GPU |  |
| `RemoteMediaResourceManager_AccessControlCheckFailed` | 1898 | WebContent -> GPU |  |
| `RemoteMediaResourceManager_DataReceived` | 1899 | WebContent -> GPU | async reply |
| `RemoteMediaResourceManager_DataSent` | 1901 | WebContent -> GPU |  |
| `RemoteMediaResourceManager_LoadFailed` | 1902 | WebContent -> GPU |  |
| `RemoteMediaResourceManager_LoadFinished` | 1903 | WebContent -> GPU |  |
| `RemoteMediaResourceManager_RedirectReceived` | 1904 | WebContent -> GPU | async reply |
| `RemoteMediaResourceManager_ResponseReceived` | 1906 | WebContent -> GPU | async reply |
| `RemoteMediaSourceProxy_AddSourceBuffer` | 4349 | WebContent -> GPU | sync |
| `RemoteMediaSourceProxy_BufferedChanged` | 1963 | WebContent -> GPU |  |
| `RemoteMediaSourceProxy_DurationChanged` | 1964 | WebContent -> GPU |  |
| `RemoteMediaSourceProxy_MarkEndOfStream` | 1965 | WebContent -> GPU |  |
| `RemoteMediaSourceProxy_SetMediaPlayerReadyState` | 1966 | WebContent -> GPU |  |
| `RemoteMediaSourceProxy_SetTimeFudgeFactor` | 1967 | WebContent -> GPU |  |
| `RemoteMediaSourceProxy_Shutdown` | 1968 | WebContent -> GPU |  |
| `RemoteMediaSourceProxy_UnmarkEndOfStream` | 1969 | WebContent -> GPU |  |
| `RemoteSourceBufferProxy_Abort` | 2110 | WebContent -> GPU |  |
| `RemoteSourceBufferProxy_AddTrackBuffer` | 2111 | WebContent -> GPU |  |
| `RemoteSourceBufferProxy_Append` | 2112 | WebContent -> GPU | async reply |
| `RemoteSourceBufferProxy_AsyncEvictCodedFrames` | 2114 | WebContent -> GPU |  |
| `RemoteSourceBufferProxy_Attach` | 2115 | WebContent -> GPU |  |
| `RemoteSourceBufferProxy_BufferedSamplesForTrackId` | 2116 | WebContent -> GPU | async reply |
| `RemoteSourceBufferProxy_CanSwitchToType` | 4352 | WebContent -> GPU | sync |
| `RemoteSourceBufferProxy_ClearTrackBuffers` | 2118 | WebContent -> GPU |  |
| `RemoteSourceBufferProxy_ComputeSeekTime` | 2119 | WebContent -> GPU | async reply |
| `RemoteSourceBufferProxy_Detach` | 2121 | WebContent -> GPU |  |
| `RemoteSourceBufferProxy_EnqueuedSamplesForTrackID` | 2122 | WebContent -> GPU | async reply |
| `RemoteSourceBufferProxy_EvictCodedFrames` | 4353 | WebContent -> GPU | sync |
| `RemoteSourceBufferProxy_MemoryPressure` | 2124 | WebContent -> GPU |  |
| `RemoteSourceBufferProxy_MinimumUpcomingPresentationTimeForTrackID` | 4354 | WebContent -> GPU | sync |
| `RemoteSourceBufferProxy_ReenqueueMediaIfNeeded` | 2125 | WebContent -> GPU |  |
| `RemoteSourceBufferProxy_RemoveCodedFrames` | 2126 | WebContent -> GPU | async reply |
| `RemoteSourceBufferProxy_RemovedFromMediaSource` | 2128 | WebContent -> GPU |  |
| `RemoteSourceBufferProxy_ResetParserState` | 2129 | WebContent -> GPU |  |
| `RemoteSourceBufferProxy_ResetTimestampOffsetInTrackBuffers` | 2130 | WebContent -> GPU |  |
| `RemoteSourceBufferProxy_ResetTrackBuffers` | 2131 | WebContent -> GPU |  |
| `RemoteSourceBufferProxy_SetActive` | 2132 | WebContent -> GPU |  |
| `RemoteSourceBufferProxy_SetAllTrackBuffersNeedRandomAccess` | 2133 | WebContent -> GPU |  |
| `RemoteSourceBufferProxy_SetAppendWindowEnd` | 2134 | WebContent -> GPU |  |
| `RemoteSourceBufferProxy_SetAppendWindowStart` | 2135 | WebContent -> GPU |  |
| `RemoteSourceBufferProxy_SetGroupStartTimestamp` | 2136 | WebContent -> GPU |  |
| `RemoteSourceBufferProxy_SetGroupStartTimestampToEndTimestamp` | 2137 | WebContent -> GPU |  |
| `RemoteSourceBufferProxy_SetMaximumBufferSize` | 2138 | WebContent -> GPU | async reply |
| `RemoteSourceBufferProxy_SetMaximumQueueDepthForTrackID` | 2140 | WebContent -> GPU |  |
| `RemoteSourceBufferProxy_SetMediaSourceEnded` | 2141 | WebContent -> GPU |  |
| `RemoteSourceBufferProxy_SetMode` | 2142 | WebContent -> GPU |  |
| `RemoteSourceBufferProxy_SetShouldGenerateTimestamps` | 2143 | WebContent -> GPU |  |
| `RemoteSourceBufferProxy_SetTimestampOffset` | 2144 | WebContent -> GPU |  |
| `RemoteSourceBufferProxy_StartChangingType` | 2145 | WebContent -> GPU |  |
| `RemoteSourceBufferProxy_UpdateTrackIds` | 2146 | WebContent -> GPU |  |
| `SourceBufferPrivateRemoteMessageReceiver_SourceBufferPrivateBufferedChanged` | 2218 | GPU -> WebContent | async reply |
| `SourceBufferPrivateRemoteMessageReceiver_SourceBufferPrivateDidAttach` | 2220 | GPU -> WebContent | async reply |
| `SourceBufferPrivateRemoteMessageReceiver_SourceBufferPrivateDidDropSample` | 2222 | GPU -> WebContent |  |
| `SourceBufferPrivateRemoteMessageReceiver_SourceBufferPrivateDidReceiveInitializationSegment` | 2223 | GPU -> WebContent | async reply |
| `SourceBufferPrivateRemoteMessageReceiver_SourceBufferPrivateDurationChanged` | 2225 | GPU -> WebContent | async reply |
| `SourceBufferPrivateRemoteMessageReceiver_SourceBufferPrivateEvictionDataChanged` | 2227 | GPU -> WebContent |  |
| `SourceBufferPrivateRemoteMessageReceiver_SourceBufferPrivateHighestPresentationTimestampChanged` | 2228 | GPU -> WebContent |  |
| `SourceBufferPrivateRemoteMessageReceiver_TakeOwnershipOfMemory` | 2229 | GPU -> WebContent |  |
| `WebBackForwardList_BackForwardItemAtIndex` | 4361 | WebContent -> UI | sync |
| `WebPageProxy_AddRemoteMediaSessionManager` | 2817 | WebContent -> UI |  |
| `WebPageProxy_CreateInspectorTarget` | 2842 | WebContent -> UI |  |
| `WebPageProxy_DestroyInspectorTarget` | 2850 | WebContent -> UI |  |
| `WebPageProxy_DidAccessWindowProxyPropertyViaOpenerForFrame` | 2851 | WebContent -> UI |  |
| `WebPageProxy_DismissDigitalCredentialsPicker` | 2914 | WebContent -> UI | async reply |
| `WebPageProxy_DocumentURLForConsoleLog` | 2917 | WebContent -> UI | async reply |
| `WebPageProxy_EnableAccessibilityForAllProcesses` | 2924 | WebContent -> UI |  |
| `WebPageProxy_GetLoadDecisionForIcon` | 2941 | WebContent -> UI |  |
| `WebPageProxy_ModelElementAnimationCurrentTime` | 2970 | WebContent -> UI | async reply |
| `WebPageProxy_ModelElementAnimationDuration` | 2972 | WebContent -> UI | async reply |
| `WebPageProxy_ModelElementGetCamera` | 2974 | WebContent -> UI | async reply |
| `WebPageProxy_ModelElementHasAudio` | 2976 | WebContent -> UI | async reply |
| `WebPageProxy_ModelElementIsLoopingAnimation` | 2978 | WebContent -> UI | async reply |
| `WebPageProxy_ModelElementIsMuted` | 2980 | WebContent -> UI | async reply |
| `WebPageProxy_ModelElementIsPlayingAnimation` | 2982 | WebContent -> UI | async reply |
| `WebPageProxy_ModelElementSetAnimationCurrentTime` | 2984 | WebContent -> UI | async reply |
| `WebPageProxy_ModelElementSetAnimationIsPlaying` | 2986 | WebContent -> UI | async reply |
| `WebPageProxy_ModelElementSetCamera` | 2988 | WebContent -> UI | async reply |
| `WebPageProxy_ModelElementSetInteractionEnabled` | 2990 | WebContent -> UI |  |
| `WebPageProxy_ModelElementSetIsLoopingAnimation` | 2991 | WebContent -> UI | async reply |
| `WebPageProxy_ModelElementSetIsMuted` | 2993 | WebContent -> UI | async reply |
| `WebPageProxy_RemoveRemoteMediaSessionManager` | 3020 | WebContent -> UI |  |
| `WebPageProxy_RequestCookieConsent` | 3025 | WebContent -> UI | async reply |
| `WebPageProxy_SetWindowFrame` | 3075 | WebContent -> UI |  |
| `WebPageProxy_ShowDigitalCredentialsPicker` | 3089 | WebContent -> UI | async reply |
| `WebPageProxy_TakeModelElementFullscreen` | 3118 | WebContent -> UI |  |
| `WebPage_DidChangeSelectedIndexForActivePopupMenu` | 3252 | Unknown -> WebContent |  |
| `WebPage_EnableAccessibility` | 3322 | Unknown -> WebContent |  |
| `WebPage_ModelInlinePreviewDidFailToLoad` | 3461 | Unknown -> WebContent |  |
| `WebPage_ModelInlinePreviewDidLoad` | 3462 | Unknown -> WebContent |  |
| `WebPage_SetMediaEnvironment` | 3637 | Unknown -> WebContent |  |
| `WebPage_SetMenuBarIsVisible` | 3639 | Unknown -> WebContent |  |
| `WebPage_SetStatusBarIsVisible` | 3668 | Unknown -> WebContent |  |
| `WebPage_SetTextForActivePopupMenu` | 3671 | Unknown -> WebContent |  |
| `WebPage_SetToolbarsAreVisible` | 3672 | Unknown -> WebContent |  |
| `WebProcessProxy_SendWasmDebuggerResponse` | 3855 | WebContent -> UI |  |
| `WebProcess_SwitchFromStaticFontRegistryToUserFontRegistry` | 3979 | UI -> WebContent |  |
| `WebResourceLoader_SetWorkerStart` | 3999 | Networking -> WebContent |  |

## Changed route or flags (6)

| Message | Old | New |
| --- | --- | --- |
| `RemoteAudioVideoRendererProxyManager_Create` | WebContent -> GPU | WebContent -> GPU, async reply |
| `RemoteAudioVideoRendererProxyManager_FlushTrack` | WebContent -> GPU | WebContent -> GPU, async reply |
| `RemoteAudioVideoRendererProxyManager_NotifyTimeReachedAndStall` | WebContent -> GPU | WebContent -> GPU, async reply |
| `RemoteAudioVideoRendererProxyManager_PrepareToSeek` | WebContent -> GPU | WebContent -> GPU, async reply |
| `RemoteMediaPlayerProxy_SeekToTarget` | WebContent -> GPU | WebContent -> GPU, async reply |
| `WebPage_StartAutoscrollAtPosition` | Unknown -> WebContent | Unknown -> WebContent, async reply |
